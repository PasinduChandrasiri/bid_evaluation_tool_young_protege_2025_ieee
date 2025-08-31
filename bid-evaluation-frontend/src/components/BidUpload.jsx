import React, { useState } from "react";
import { useAuth } from "../contexts/AuthContext";
import { uploadBid } from "../api/api";

export default function BidUpload() {
  const { user } = useAuth();
  const [bidderName, setBidderName] = useState("");
  const [price, setPrice] = useState("");
  const [tenderId, setTenderId] = useState("");
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleUpload = async (e) => {
    e.preventDefault();
    setMessage("");
    if (!bidderName || !price || !tenderId || !file) {
      setMessage("Fill all fields and choose a file.");
      return;
    }
    try {
      const formData = new FormData();
      formData.append("tender_id", tenderId);
      formData.append("bidder_name", bidderName);
      formData.append("price", price);
      formData.append("file", file);
      await uploadBid(formData, user.token);
      setMessage("Bid uploaded successfully!");
    } catch (err) {
      setMessage(`Upload failed: ${err.message}`);
    }
  };

  return (
    <div>
      <h2>Upload Bid Submission</h2>
      <form onSubmit={handleUpload}>
        <label>Tender ID: </label>
        <input value={tenderId} onChange={e => setTenderId(e.target.value)} required /><br />
        <label>Bidder Name: </label>
        <input value={bidderName} onChange={e => setBidderName(e.target.value)} required /><br />
        <label>Price: </label>
        <input type="number" value={price} onChange={e => setPrice(e.target.value)} required /><br />
        <label>File: </label>
        <input type="file" onChange={e => setFile(e.target.files[0])} required /><br />
        <button type="submit">Upload</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}
