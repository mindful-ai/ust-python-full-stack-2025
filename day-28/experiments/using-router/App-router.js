import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function App() {
  return (
    <Router>
      <div style={{ padding: 20 }}>
        {/* Navigation */}
        <nav style={{ marginBottom: 20 }}>
          <Link to="/" style={{ marginRight: 10 }}>Home</Link>
          <Link to="/about" style={{ marginRight: 10 }}>About</Link>
          <Link to="/contact">Contact</Link>
        </nav>

        {/* Route Definitions */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </div>
    </Router>
  );
}

/* Page Components */
function Home() {
  return <h2>Welcome to the Home Page</h2>;
}

function About() {
  return <h2>About Us: We build great apps!</h2>;
}

function Contact() {
  return <h2>Contact Us at: support@example.com</h2>;
}

export default App;
