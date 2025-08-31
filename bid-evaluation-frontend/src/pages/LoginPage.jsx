import React, { useState } from "react";
import { useAuth } from "../contexts/AuthContext";
import { login } from "../api/api";

export default function LoginPage() {
  const { login: authLogin } = useAuth();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);

  const handleSubmit = async(e) => {
    e.preventDefault();
    try {
      const data = await login({ username, password });
      authLogin({ username, token: data.access_token });
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <div style={{ maxWidth: 320, margin: "auto", paddingTop: 120 }}>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" required />
        <br />
        <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" required />
        <br />
        <button type="submit">Login</button>
        {error && <p style={{color:'red'}}>{error}</p>}
      </form>
    </div>
  );
}
