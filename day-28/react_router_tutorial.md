# React Router Quick Tutorial

## 1. Installation

``` bash
npm install react-router-dom
```

## 2. Basic Setup

``` jsx
import { BrowserRouter as Router } from "react-router-dom";

function App() {
  return (
    <Router>
      {/* Your app structure */}
    </Router>
  );
}
```

## 3. Creating Routes

``` jsx
import { Routes, Route } from "react-router-dom";

<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/products" element={<Products />} />
</Routes>
```

## 4. Navigation Links

``` jsx
<Link to="/">Home</Link>
<Link to="/products">Products</Link>
```

## 5. Layouts With Outlet

``` jsx
function Layout() {
  return (
    <>
      <Header />
      <Outlet />
      <Footer />
    </>
  );
}
```

## 6. Programmatic Navigation

``` jsx
const navigate = useNavigate();
navigate("/dashboard");
```

## 7. URL Params

``` jsx
const { id } = useParams();
```

## 8. Query Params

``` jsx
const [params] = useSearchParams();
params.get("sort");
```

## 9. 404 Route

``` jsx
<Route path="*" element={<h2>Page Not Found</h2>} />
```
