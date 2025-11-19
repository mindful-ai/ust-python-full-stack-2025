export const API = "http://localhost:8000";

export async function api(path, method = "GET", body = null) {
  const res = await fetch(API + path, {
    method,
    headers: { "Content-Type": "application/json" },
    body: body ? JSON.stringify(body) : null,
  });
  return res.json();
}
