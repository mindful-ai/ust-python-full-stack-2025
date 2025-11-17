import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Header from "./components/Header";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

// View Components
import Dashboard from "./views/Dashboard/Dashboard";
import Incidents from "./views/Incidents/Incidents";
import Customers from "./views/Customers/Customers";
import About from "./views/About/About";

function App() {
  return (
    <Router>
      <div style={{ display: "flex", flexDirection: "column", minHeight: "100vh" }}>

        <Header />
        <Navbar />

        <main style={{ flex: 1, padding: "20px" }}>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/incidents" element={<Incidents />} />
            <Route path="/customers" element={<Customers />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </main>

        <Footer />

      </div>
    </Router>
  );
}

export default App;
