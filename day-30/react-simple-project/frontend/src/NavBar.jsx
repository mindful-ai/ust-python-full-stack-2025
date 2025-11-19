import React from "react";
import { Link, useNavigate } from "react-router-dom";

export default function NavBar() {
  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  const logout = () => {
    localStorage.clear();
    navigate("/login");
  };

  return (
    <nav className="bg-blue-700 text-white px-6 py-3 shadow-md">
      <div className="flex justify-between items-center">

        {/* Left section */}
        <div className="flex items-center gap-6 text-lg font-medium">
          <Link className="hover:text-gray-200 transition" to="/">Dashboard</Link>
          <Link className="hover:text-gray-200 transition" to="/incidents">Incidents</Link>
          <Link className="hover:text-gray-200 transition" to="/customers">Customers</Link>
          <Link className="hover:text-gray-200 transition" to="/about">About</Link>
        </div>

        {/* Right section */}
        <div>
          {!token ? (
            <Link
              to="/login"
              className="bg-white text-blue-700 px-4 py-1 rounded hover:bg-gray-200 transition"
            >
              Login
            </Link>
          ) : (
            <button
              onClick={logout}
              className="bg-red-500 px-4 py-1 rounded hover:bg-red-600 transition"
            >
              Logout
            </button>
          )}
        </div>
      </div>
    </nav>
  );
}
