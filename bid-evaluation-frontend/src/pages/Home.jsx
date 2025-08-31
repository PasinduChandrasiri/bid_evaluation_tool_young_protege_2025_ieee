import React from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";

export default function Home() {
  const { user } = useAuth();
  return (
    <div style={{ padding: "2rem" }}>
      <h1>Bid Evaluation Dashboard</h1>
      {user ? (
        <>
          <p>Welcome, <strong>{user.username}</strong>!</p>
          <ul>
            <li><Link to="/upload-bid">Upload Bid</Link></li>
            <li><Link to="/committee-review">Committee Review</Link></li>
            <li><Link to="/dashboard">Comprehensive Dashboard</Link></li>
          </ul>
        </>
      ) : (
        <p><Link to="/login">Login</Link> to access system features.</p>
      )}
    </div>
  );
}
