import React, { useState } from "react";

function App() {
  const [msg, setMsg] = useState("");

  const pingServer = async () => {
    const res = await fetch(`${process.env.REACT_APP_API_BASE}/ping`);
    const data = await res.json();
    setMsg(data.message);
  };

  return (
    <div>
      <h1>Aadee MultiAgent</h1>
      <button onClick={pingServer}>Ping Backend</button>
      {msg && <p>{msg}</p>}
    </div>
  );
}

export default App;
