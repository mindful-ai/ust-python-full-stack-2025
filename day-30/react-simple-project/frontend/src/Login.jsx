import React, { useState } from "react";
import { api } from "./api";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [form, setForm] = useState({});
  const navigate = useNavigate();

  const submit = async () => {
    const res = await api("/login", "POST", form);
    localStorage.setItem("token", res.token);
    localStorage.setItem("username", res.username);
    navigate("/");
  };

  return (
    <div>
      <h2 className="text-xl mb-2">Login</h2>
      <input className="border p-2 block mb-2" placeholder="Username"
        onChange={(e) => setForm({ ...form, username: e.target.value })} />
      <input className="border p-2 block mb-2" placeholder="Password"
        onChange={(e) => setForm({ ...form, password: e.target.value })} />

      <button className="bg-blue-500 text-white px-4 py-2" onClick={submit}>Login</button>
    </div>
  );
}
