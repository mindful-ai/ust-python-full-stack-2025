import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Box } from "@mui/material";

import Header from "./components/Header";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

import Dashboard from "./views/Dashboard/Dashboard";
import Bangalore from "./views/Dashboard/Bangalore";
import Hyderabad from "./views/Dashboard/Hyderabad";
import Chennai from "./views/Dashboard/Chennai";
import Trivandrum from "./views/Dashboard/Trivandrum";


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

            {/* Dashboard with nested routes */}
            <Route path="/dashboard" element={<Dashboard />}>
              <Route path="bangalore" element={<Bangalore />} />
              <Route path="hyderabad" element={<Hyderabad />} />
              <Route path="chennai" element={<Chennai />} />
              <Route path="trivandrum" element={<Trivandrum />} />
            </Route>

            {/* Other Top-Level Routes */}
            <Route path="/incidents" element={<Incidents />} />
            <Route path="/customers" element={<Customers />} />
            <Route path="/about" element={<About />} />

            {/* Default → dashboard/bangalore */}
            <Route path="/" element={<Dashboard />} />
          </Routes>
        </Box>

        <Footer />

      </Box>
    </Router>
  );
}

export default App;
