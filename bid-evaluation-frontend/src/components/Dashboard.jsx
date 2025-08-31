import React, { useEffect, useState } from "react";
import { useAuth } from "../contexts/AuthContext";

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000';

async function fetchBids(token, tenderId) {
  const res = await fetch(`${API_BASE}/bids/tender/${tenderId}`, {
    headers: { "Authorization": `Bearer ${token}` }
  });
  if (!res.ok) throw new Error("Failed to fetch bids.");
  return res.json();
}

export default function Dashboard() {
  const { user } = useAuth();
  const [tenderId, setTenderId] = useState("1");
  const [bids, setBids] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    if (user?.token && tenderId) {
      fetchBids(user.token, tenderId)
        .then(setBids)
        .catch(e => setError(e.message));
    }
  }, [user, tenderId]);

  return (
    <div>
      <h2>Bids Dashboard</h2>
      <label>Tender ID: </label>
      <input value={tenderId} onChange={e => setTenderId(e.target.value)} />
      <button onClick={() => fetchBids(user.token, tenderId).then(setBids).catch(e => setError(e.message))}>
        Refresh
      </button>
      {error && <p style={{color: "red"}}>{error}</p>}
      {bids.length === 0 ? (
        <p>No bids yet for this tender.</p>
      ) : (
        <table border="1">
          <thead>
            <tr>
              <th>Bid ID</th>
              <th>Bidder Name</th>
              <th>Price</th>
              <th>Status</th>
              <th>Bid Document</th>
              <th>Uploaded At</th>
            </tr>
          </thead>
          <tbody>
            {bids.map(bid => (
              <tr key={bid.id}>
                <td>{bid.id}</td>
                <td>{bid.bidder_name}</td>
                <td>{bid.price}</td>
                <td>{bid.status}</td>
                <td>
                  <a href={bid.bid_document_url || bid.bid_document} target="_blank" rel="noopener noreferrer">
                    Download
                  </a>
                </td>
                <td>{bid.uploaded_at}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
