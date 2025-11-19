import React, { useState } from "react";
import { api } from "./api";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const [form, setForm] = useState({});
  const navigate = useNavigate();

  const submit = async () => {
    await api("/register", "POST", form);
    navigate("/login");
  };

  return (
    <div>
      <h2 className="text-xl mb-2">Register</h2>
      <input className="border p-2 block mb-2" placeholder="Username"
        onChange={(e) => setForm({ ...form, username: e.target.value })} />
      <input className="border p-2 block mb-2" placeholder="Password"
        onChange={(e) => setForm({ ...form, password: e.target.value })} />

      <button className="bg-blue-500 text-white px-4 py-2" onClick={submit}>Register</button>
    </div>
  );
}
