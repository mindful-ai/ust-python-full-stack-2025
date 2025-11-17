// import { Box } from "@mui/material";
// import { Outlet } from "react-router-dom";
// import DashboardNav from "./DashboardNav";

// export default function Dashboard() {
//   return (
//     <Box display="flex">
      
//       {/* Left Navigation Drawer */}
//       <DashboardNav />

//       {/* Right Content Area - child routes appear in this area <outlet> */}
//       <Box flex={1} p={3}>
//         <Outlet />
//       </Box>
//     </Box>
//   );
// }

import { Box, Paper } from "@mui/material";
import { Outlet } from "react-router-dom";
import DashboardNav from "./DashboardNav";

export default function Dashboard() {
  return (
    <Box 
      display="flex" 
      gap={2}
      p={2}
      sx={{ height: "100%", boxSizing: "border-box" }}
    >
      {/* Mini Sidebar */}
      <Paper
        elevation={2}
        sx={{
          width: 70,
          minWidth: 70,
          height: "auto",
          padding: "10px 0",
          borderRadius: 2,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: 2,
          position: "relative",     // stays inside container
        }}
      >
        <DashboardNav />
      </Paper>

      {/* Right content area */}
      <Box flex={1}>
        <Outlet />
      </Box>
    </Box>
  );
}
