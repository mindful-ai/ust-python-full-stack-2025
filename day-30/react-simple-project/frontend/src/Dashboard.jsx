import React, { useEffect, useState } from "react";
import { Bar, Pie } from "react-chartjs-2";
import { api } from "./api";
import "chart.js/auto";

export default function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    api("/chart-data").then(setData);
  }, []);

  if (!data) return <p>Loading...</p>;

  return (
    <div className="grid grid-cols-2 gap-8">
      <div>
        <h2 className="text-xl mb-2">Incidents by City (Bar)</h2>
        <Bar
          data={{
            labels: data.cities,
            datasets: [{ label: "Incidents", data: data.values }],
          }}
        />
      </div>

      <div>
        <h2 className="text-xl mb-2">Distribution (Pie)</h2>
        <Pie
          data={{
            labels: data.cities,
            datasets: [{ data: data.values }],
          }}
        />
      </div>
    </div>
  );
}
