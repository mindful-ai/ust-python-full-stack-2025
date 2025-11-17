import { Box, Typography } from "@mui/material";

export default function Footer() {
  return (
    <Box 
      sx={{ 
        background: "#222", 
        color: "#fff", 
        padding: 2, 
        textAlign: "center",
        marginTop: "auto"
      }}
    >
      <Typography variant="body2">© 2025 My React App</Typography>
    </Box>
  );
}

