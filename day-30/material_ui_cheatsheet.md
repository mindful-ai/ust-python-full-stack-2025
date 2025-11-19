# Material UI (MUI) Cheat Sheet

## 🎨 Install MUI

``` bash
npm install @mui/material @emotion/react @emotion/styled
npm install @mui/icons-material
```

## 🟦 Import Basics

``` jsx
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
```

## 🔘 Buttons

``` jsx
<Button variant="text">Text</Button>
<Button variant="contained">Contained</Button>
<Button variant="outlined">Outlined</Button>
```

With icons:

``` jsx
<Button startIcon={<DeleteIcon />}>Delete</Button>
```

## ✏️ TextField

``` jsx
<TextField label="Email" variant="outlined" fullWidth />
```

## 🔲 Layout (Box & Grid)

``` jsx
<Box sx={{ p: 2, display: "flex", gap: 2 }}></Box>

<Grid container spacing={2}>
  <Grid item xs={12} md={6}></Grid>
</Grid>
```

## 🎛️ Select

``` jsx
<Select value={age} onChange={handleChange}>
  <MenuItem value={10}>Ten</MenuItem>
</Select>
```

## 🎚️ Switch, Checkbox, Radio

``` jsx
<Switch defaultChecked />
<Checkbox defaultChecked />
<RadioGroup>
  <FormControlLabel value="a" control={<Radio />} label="Option A" />
</RadioGroup>
```

## 🧱 Card

``` jsx
<Card sx={{ maxWidth: 300, p: 2 }}>
  <CardContent>
    <Typography variant="h5">Title</Typography>
    <Typography>Card description goes here.</Typography>
  </CardContent>
</Card>
```

## 🧭 AppBar

``` jsx
<AppBar position="static">
  <Toolbar>
    <Typography variant="h6">My App</Typography>
  </Toolbar>
</AppBar>
```

## 🎨 Styling with sx

``` jsx
<Box sx={{ bgcolor: "primary.main", p: 2 }}></Box>

<Button
  variant="contained"
  sx={{ backgroundColor: "green", "&:hover": { backgroundColor: "darkgreen" } }}
>
  Save
</Button>
```

Responsive:

``` jsx
<Box sx={{ fontSize: { xs: 14, md: 20 } }}></Box>
```

## 🪟 Dialog

``` jsx
<Dialog open={open} onClose={handleClose}>
  <DialogTitle>Confirm</DialogTitle>
  <DialogContent>Are you sure?</DialogContent>
  <DialogActions>
    <Button onClick={handleClose}>Cancel</Button>
  </DialogActions>
</Dialog>
```

## 📊 Table

``` jsx
<Table>
  <TableHead>
    <TableRow>
      <TableCell>Name</TableCell>
      <TableCell>Age</TableCell>
    </TableRow>
  </TableHead>
  <TableBody>
    <TableRow>
      <TableCell>John</TableCell>
      <TableCell>30</TableCell>
    </TableRow>
  </TableBody>
</Table>
```

## 🎨 Theme Example

``` jsx
const theme = createTheme({
  palette: {
    primary: { main: "#1976d2" },
    secondary: { main: "#9c27b0" },
  },
});
```

## 🧩 Common Components List

-   Button\
-   TextField\
-   Select\
-   Card\
-   AppBar\
-   Drawer\
-   Dialog\
-   Tabs\
-   Snackbar\
-   Table
