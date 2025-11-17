// import { Drawer, List, ListItemButton, ListItemText } from "@mui/material";
// import { Link } from "react-router-dom";

// const cities = [
//   "bangalore",
//   "hyderabad",
//   "chennai",
//   "trivandrum",

// ];

// export default function DashboardNav() {
//   return (
//     <Drawer
//       variant="permanent"
//       sx={{
//         width: 200,
//         flexShrink: 0,
//         [`& .MuiDrawer-paper`]: { width: 200, boxSizing: "border-box" },
//       }}
//     >
//       <List>
//         {cities.map((city) => (
//           <ListItemButton
//             key={city}
//             component={Link}
//             to={`/dashboard/${city}`}
//           >
//             <ListItemText primary={city.charAt(0).toUpperCase() + city.slice(1)} />
//           </ListItemButton>
//         ))}
//       </List>
//     </Drawer>
//   );
// }

import { Box, Button, Tooltip } from "@mui/material";
import { useNavigate } from "react-router-dom";

export default function DashboardNav() {
  const navigate = useNavigate();

  const menu = [
    { label: "BLR", path: "bangalore" },
    { label: "HYD", path: "hyderabad" },
    { label: "CHN", path: "chennai" },
    { label: "TVM", path: "trivandrum" },
  ];

  return (
    <Box display="flex" flexDirection="column" gap={1} alignItems="center">
      {menu.map((item) => (
        <Tooltip key={item.path} title={item.label} placement="right">
          <Button
            variant="outlined"
            size="small"
            sx={{
              minWidth: "40px",
              width: "40px",
              height: "40px",
              borderRadius: "12px",
              padding: 0,
            }}
            onClick={() => navigate(`/dashboard/${item.path}`)}
          >
            {item.label}
          </Button>
        </Tooltip>
      ))}
    </Box>
  );
}
