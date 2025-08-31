import React, { useState } from "react";
import { useAuth } from "../contexts/AuthContext";
import { login } from "../api/api";

export default function Login() {
  const { login: authLogin } = useAuth();
  const [form, setForm] = useState({ username: "", password: "" });
  const [error, setError] = useState("");

  const handleChange = e => setForm(f => ({
    ...f, [e.target.name]: e.target.value
  }));

  const handleSubmit = async e => {
    e.preventDefault();
    setError("");
    try {
      const data = await login(form);
      authLogin({ username: form.username, token: data.access_token });
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      <input name="username" value={form.username} onChange={handleChange} placeholder="Username" required />
      <input name="password" type="password" value={form.password} onChange={handleChange} placeholder="Password" required />
      <button type="submit">Login</button>
      {error && <p style={{color: "red"}}>{error}</p>}
    </form>
  );
}
