// Placeholder App.js
import React from "react";
import { Routes, Route } from "react-router-dom";
import NavBar from "./NavBar";
import Dashboard from "./Dashboard";
import Incidents from "./Incidents";
import Customers from "./Customers";
import About from "./About";
import Login from "./Login";
import Register from "./Register";

function App() {
  return (
    <div>
      <NavBar />
      <div className="p-4">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/incidents" element={<Incidents />} />
          <Route path="/customers" element={<Customers />} />
          <Route path="/about" element={<About />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
