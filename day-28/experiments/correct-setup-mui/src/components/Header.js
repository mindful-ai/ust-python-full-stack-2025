import { AppBar, Toolbar, Typography } from "@mui/material";

export default function Header() {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6">My MUI React App</Typography>
      </Toolbar>
    </AppBar>
  );
}

