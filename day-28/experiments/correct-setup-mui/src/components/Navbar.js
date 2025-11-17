import { AppBar, Toolbar, Button } from "@mui/material";
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <AppBar position="static" color="secondary">
      <Toolbar>
        <Button component={Link} to="/" color="inherit">Dashboard</Button>
        <Button component={Link} to="/incidents" color="inherit">Incidents</Button>
        <Button component={Link} to="/customers" color="inherit">Customers</Button>
        <Button component={Link} to="/about" color="inherit">About</Button>
      </Toolbar>
    </AppBar>
  );
}

