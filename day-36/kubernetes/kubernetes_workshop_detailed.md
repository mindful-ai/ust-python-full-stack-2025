# Kubernetes Workshop on Docker Desktop (2 Hours)

Hands-on introduction to Kubernetes using **Docker Desktop’s built-in Kubernetes**. Designed for professionals who know basic Docker.

---

## Learning Outcomes
By the end, participants will be able to:
- Explain Pods, Deployments, and Services.
- Deploy an app, expose it, scale it, and roll it back.
- Use `kubectl` to inspect, debug, and clean up workloads.

---

## Prerequisites
- Docker Desktop installed. Enable **Settings → Kubernetes → Enable Kubernetes**.
- `kubectl` available on PATH (bundled with Docker Desktop).
- Verify:
  ```bash
  kubectl version --client
  kubectl cluster-info
  kubectl get nodes
  ```

---

## 1) Kubernetes Core Concepts (15 min)

- **Pod**: Smallest deployable unit (1+ containers, shared network/storage).
- **Deployment**: Declarative manager that keeps Pods at desired replicas and supports **rolling updates**/**rollbacks**.
- **Service**: Stable virtual IP in-cluster; types:
  - `ClusterIP` (default, internal only)
  - `NodePort` (exposes port on node/localhost for Docker Desktop)
  - `LoadBalancer` (cloud only; not used in this local lab)
- **ConfigMap/Secret**: Externalize configuration.
- **Namespace**: Logical partitioning of resources.

Useful commands:
```bash
kubectl get all -n kube-system
kubectl api-resources
kubectl explain deployment.spec.template.spec.containers
```

---

## 2) Lab: Nginx Deployment + NodePort Service (45 min)

### Files
`nginx-deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.25-alpine
        ports:
        - containerPort: 80
        readinessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 10
        livenessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 10
          periodSeconds: 20
```

Apply and verify:
```bash
kubectl apply -f nginx-deployment.yaml
kubectl get deployments
kubectl get pods -o wide
kubectl describe deployment nginx-deployment
```

`nginx-service.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
  - name: http
    port: 80
    targetPort: 80
    nodePort: 30080
```

Expose and test:
```bash
kubectl apply -f nginx-service.yaml
kubectl get svc nginx-service
# Visit in browser:
# http://localhost:30080
```

**Key Talking Points:**
- Probes add self‑healing & safe rollouts.
- `NodePort` works locally on Docker Desktop; no cloud LB needed.

---

## 3) Scaling, Rolling Updates, and Rollbacks (25 min)

**Scale up:**
```bash
kubectl scale deployment nginx-deployment --replicas=5
kubectl get pods
```

**Rolling update to a new version:**
```bash
kubectl set image deployment/nginx-deployment \
  nginx=nginx:1.27-alpine
kubectl rollout status deployment/nginx-deployment
```

**Check rollout & history:**
```bash
kubectl rollout history deployment/nginx-deployment
kubectl describe deploy/nginx-deployment | grep -i image
```

**Rollback (if needed):**
```bash
kubectl rollout undo deployment/nginx-deployment
```

---

## 4) Live Debugging with `kubectl` (15 min)

```bash
kubectl get pods -o wide
kubectl logs -l app=nginx --tail=50
kubectl exec -it deploy/nginx-deployment -- sh -c 'nginx -v || cat /etc/os-release'
kubectl describe pod $(kubectl get pods -l app=nginx -o name | head -n1)
```

**Port-forward (alt to NodePort):**
```bash
kubectl port-forward deploy/nginx-deployment 8080:80
# http://localhost:8080
```

---

## 5) Optional: ConfigMap for Custom Index (10 min)

`index-configmap.yaml`
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-index
data:
  index.html: |
    <html><body><h1>Hello from Kubernetes on Docker Desktop!</h1></body></html>
```

`nginx-deployment-with-cm.yaml` (snippet)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-cm
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx-cm
  template:
    metadata:
      labels:
        app: nginx-cm
    spec:
      containers:
      - name: nginx
        image: nginx:1.25-alpine
        volumeMounts:
        - name: webroot
          mountPath: /usr/share/nginx/html/index.html
          subPath: index.html
      volumes:
      - name: webroot
        configMap:
          name: nginx-index
```

Apply and test:
```bash
kubectl apply -f index-configmap.yaml
kubectl apply -f nginx-deployment-with-cm.yaml
kubectl expose deployment nginx-cm --type=NodePort --port=80
kubectl get svc
# Open the NodePort in the browser.
```

---

## 6) Cleanup (5 min)

```bash
kubectl delete -f nginx-deployment.yaml
kubectl delete -f nginx-service.yaml
kubectl delete -f index-configmap.yaml || true
kubectl delete -f nginx-deployment-with-cm.yaml || true
```

---

## Troubleshooting Tips
- Pod stuck `ImagePullBackOff` → check image name & network access.
- Pod `CrashLoopBackOff` → inspect `kubectl logs` and `kubectl describe pod`.
- Service not reachable → confirm `NodePort` and container `containerPort` match, verify Pods are `READY`.
- Use `kubectl get events --sort-by=.lastTimestamp` for recent cluster events.

---

## Quick Reference

```bash
# Core
kubectl get nodes,pods,svc,deploy
kubectl describe deploy/<name>
kubectl logs deploy/<name>

# Scale & rollouts
kubectl scale deploy/<name> --replicas=3
kubectl set image deploy/<name> <container>=<image:tag>
kubectl rollout status deploy/<name>
kubectl rollout undo deploy/<name>

# Port-forward
kubectl port-forward deploy/<name> 8080:80

# Delete
kubectl delete -f <file.yaml>
```

**Next Steps:** Ingress, Secrets, StatefulSets, PVC/PV, and Helm.