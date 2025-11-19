import React, { useEffect, useState } from "react";
import { api } from "./api";

export default function Incidents() {
  const [incident, setIncident] = useState({
    type: "",
    city: "",
    description: "",
  });
  const [list, setList] = useState([]);

  useEffect(() => {
    api("/incidents").then(setList);
  }, []);

  const submit = async () => {
    if (!localStorage.getItem("token")) {
      alert("Login first!");
      return;
    }
    await api("/incidents", "POST", incident);
    const updated = await api("/incidents");
    setList(updated);
  };

  return (
    <div>
      <h2 className="text-xl mb-2">Add Incident</h2>

      <div className="flex gap-2 mb-4">
        <input
          placeholder="Type"
          className="border p-2"
          onChange={(e) => setIncident({ ...incident, type: e.target.value })}
        />
        <input
          placeholder="City"
          className="border p-2"
          onChange={(e) => setIncident({ ...incident, city: e.target.value })}
        />
        <input
          placeholder="Description"
          className="border p-2"
          onChange={(e) =>
            setIncident({ ...incident, description: e.target.value })
          }
        />
        <button className="bg-blue-500 text-white px-3" onClick={submit}>
          Add
        </button>
      </div>

      <h3 className="text-lg mb-1">Incident List</h3>
      <ul>
        {list.map((i) => (
          <li key={i.id}>
            {i.id}. {i.type} - {i.city} ({i.description})
          </li>
        ))}
      </ul>
    </div>
  );
}
