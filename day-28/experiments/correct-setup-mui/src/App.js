import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Box } from "@mui/material";

import Header from "./components/Header";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

// Views
import Dashboard from "./views/Dashboard/Dashboard";
import Incidents from "./views/Incidents/Incidents";
import Customers from "./views/Customers/Customers";
import About from "./views/About/About";

function App() {
  return (
    <Router>
      <Box display="flex" flexDirection="column" minHeight="100vh">
        
        <Header />
        <Navbar />

        <Box flex={1} mt={2}>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/incidents" element={<Incidents />} />
            <Route path="/customers" element={<Customers />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </Box>

        <Footer />

      </Box>
    </Router>
  );
}

export default App;
