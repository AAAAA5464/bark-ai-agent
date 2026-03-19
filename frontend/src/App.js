import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [leads, setLeads] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/leads")
      .then(res => {
        console.log(res.data);   // 👈 DEBUG
        setLeads(res.data);
      })
      .catch(err => console.log(err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>🔥 Bark Lead Dashboard</h1>

      {leads.length === 0 ? (
        <p>Loading...</p>
      ) : (
        leads.map((lead, i) => (
          <div key={i} style={{
            border: "1px solid gray",
            padding: "10px",
            margin: "10px"
          }}>
            <h2>{lead.title}</h2>
            <p><b>Score:</b> {lead.score}</p>
            <p><b>Reason:</b> {lead.reason}</p>
            <p><b>Pitch:</b> {lead.pitch}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default App;