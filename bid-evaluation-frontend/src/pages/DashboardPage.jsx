import React, { useEffect, useState } from "react";
import { useAuth } from "../contexts/AuthContext";
import { uploadBid, approveBid } from "../api/api";

export default function DashboardPage() {
  const { user, logout } = useAuth();
  const [file, setFile] = useState(null);
  const [bidderName, setBidderName] = useState("");
  const [price, setPrice] = useState("");
  const [tenderId, setTenderId] = useState(1); // Hardcoded for demo
  const [message, setMessage] = useState("");

  const handleFileChange = e => setFile(e.target.files[0]);

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file || !bidderName || !price) {
      setMessage("Please fill all fields and select a file.");
      return;
    }
    try {
      const formData = new FormData();
      formData.append("file", file);
      formData.append("bidder_name", bidderName);
      formData.append("price", price);
      formData.append("tender_id", tenderId);

      await uploadBid(formData, user.token);
      setMessage("Bid uploaded successfully.");
    } catch (err) {
      setMessage(`Error: ${err.message}`);
    }
  };

  const handleApprove = async () => {
    // For demo: Approve bid with id = 1 (hardcoded)
    try {
      const blob = await approveBid(1, user.token);
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "LetterOfAcceptance.pdf";
      document.body.appendChild(a);
      a.click();
      a.remove();
      setMessage("Letter of Acceptance downloaded.");
    } catch (err) {
      setMessage(`Error: ${err.message}`);
    }
  };

  return (
    <div style={{ margin: 20 }}>
      <h1>Welcome, {user.username}</h1>
      <button onClick={logout}>Logout</button>

      <h2>Upload Bid</h2>
      <form onSubmit={handleUpload}>
        <input type="text" placeholder="Bidder Name" value={bidderName} onChange={e=>setBidderName(e.target.value)} required />
        <br />
        <input type="number" placeholder="Bid Price" value={price} onChange={e=>setPrice(e.target.value)} required />
        <br />
        <input type="file" onChange={handleFileChange} required />
        <br />
        <button type="submit">Upload Bid</button>
      </form>

      <h2>Approve Bid (demo)</h2>
      <button onClick={handleApprove}>Generate & Download Letter of Acceptance (Bid ID 1)</button>

      {message && <p>{message}</p>}
    </div>
  );
}
