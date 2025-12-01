# Nginx-Based Serving for Flask on AWS EC2

## 1. Install Nginx

``` bash
sudo apt update
sudo apt install nginx -y
```

## 2. Install and Test Gunicorn

``` bash
pip install gunicorn
gunicorn --bind 0.0.0.0:5000 app:app
```

## 3. Create Gunicorn systemd Service

Create file:

``` bash
sudo nano /etc/systemd/system/flask.service
```

Add:

    [Unit]
    Description=Gunicorn instance to serve Flask
    After=network.target

    [Service]
    User=ubuntu
    Group=www-data
    WorkingDirectory=/home/ubuntu/your-flask-folder
    Environment="PATH=/home/ubuntu/your-flask-folder/venv/bin"
    ExecStart=/home/ubuntu/your-flask-folder/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/your-flask-folder/flask.sock app:app

    [Install]
    WantedBy=multi-user.target

Start service:

``` bash
sudo systemctl daemon-reload
sudo systemctl start flask
sudo systemctl enable flask
```

## 4. Configure Nginx

Create config:

``` bash
sudo nano /etc/nginx/sites-available/flaskapp
```

Add:

    server {
        listen 80;
        server_name _;

        location / {
            proxy_pass http://unix:/home/ubuntu/your-flask-folder/flask.sock;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }

Enable:

``` bash
sudo ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
```

Test and restart:

``` bash
sudo nginx -t
sudo systemctl restart nginx
```

## 5. EC2 Security Group

Allow inbound: - HTTP (80)

Access:

    http://EC2-PUBLIC-IP
