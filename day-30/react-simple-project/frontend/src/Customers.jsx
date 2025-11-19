import React, { useEffect, useState } from "react";
import { api } from "./api";

export default function Customers() {
  const [customers, setCustomers] = useState([]);

  useEffect(() => {
    api("/customers").then(setCustomers);
  }, []);

  return (
    <div>
      <h2 className="text-xl mb-3">Customers</h2>
      <table className="border">
        <thead>
          <tr className="border">
            <th className="border p-2">ID</th>
            <th className="border p-2">Name</th>
            <th className="border p-2">Email</th>
          </tr>
        </thead>

        <tbody>
          {customers.map((c) => (
            <tr key={c.id}>
              <td className="border p-2">{c.id}</td>
              <td className="border p-2">{c.name}</td>
              <td className="border p-2">{c.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
