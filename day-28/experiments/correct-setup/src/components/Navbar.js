import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav style={{ background: "#e3e3e3", padding: "10px" }}>
      <Link to="/" style={{ marginRight: 15 }}>Dashboard</Link>
      <Link to="/incidents" style={{ marginRight: 15 }}>Incidents</Link>
      <Link to="/customers" style={{ marginRight: 15 }}>Customers</Link>
      <Link to="/about">About</Link>
    </nav>
  );
}
