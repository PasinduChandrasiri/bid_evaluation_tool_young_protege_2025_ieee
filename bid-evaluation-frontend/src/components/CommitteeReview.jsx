import React, { useEffect, useState } from "react";
import { useAuth } from "../contexts/AuthContext";

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000';

async function fetchEvaluations(token) {
  const res = await fetch(`${API_BASE}/committee/evaluations`, {
    headers: { "Authorization": `Bearer ${token}` }
  });
  if (!res.ok) throw new Error("Failed to fetch evaluations.");
  return res.json();
}

async function approveBid(bidId, token) {
  const res = await fetch(`${API_BASE}/committee/approve/${bidId}`, {
    method: "POST",
    headers: { "Authorization": `Bearer ${token}` }
  });
  if (!res.ok)
    throw new Error("Approval failed.");
  const blob = await res.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `LetterOfAcceptance_Bid${bidId}.pdf`;
  a.click();
  URL.revokeObjectURL(url);
}

export default function CommitteeReview() {
  const { user } = useAuth();
  const [evaluations, setEvaluations] = useState([]);
  const [message, setMessage] = useState("");

  useEffect(() => {
    if (user?.token) {
      fetchEvaluations(user.token)
        .then(setEvaluations)
        .catch(e => setMessage(e.message));
    }
  }, [user]);

  const handleApprove = async (bidId) => {
    try {
      await approveBid(bidId, user.token);
      setMessage("Letter of Acceptance downloaded.");
    } catch (e) {
      setMessage(e.message);
    }
  };

  return (
    <div>
      <h2>Committee Review - Evaluate and Approve Bids</h2>
      {evaluations.length === 0 ? (
        <p>No bid evaluations to display.</p>
      ) : (
        <table border="1">
          <thead>
            <tr>
              <th>Bid ID</th>
              <th>Prelim Check</th>
              <th>Detail Score</th>
              <th>Post Qualification</th>
              <th>Notes</th>
              <th>Approve</th>
            </tr>
          </thead>
          <tbody>
            {evaluations.map(ev => (
              <tr key={ev.id}>
                <td>{ev.bid_id}</td>
                <td>{ev.prelim_check ? "Yes" : "No"}</td>
                <td>{ev.detail_score || "-"}</td>
                <td>{ev.post_qualification ? "Yes" : "No"}</td>
                <td>{ev.evaluation_notes}</td>
                <td>
                  <button onClick={() => handleApprove(ev.bid_id)}>Approve/Download PDF</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
      {message && <p>{message}</p>}
    </div>
  );
}
