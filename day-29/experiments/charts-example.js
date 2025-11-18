import React from "react";
import { Bar, Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Tooltip,
  Legend
} from "chart.js";

// Register chart components
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Tooltip,
  Legend
);

function App() {

  // ---------------------------------------------

   const barData = {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [
      {
        label: "Sample Values",
        data: [12, 19, 3, 5, 2, 3],
        backgroundColor: [
          "rgba(255, 99, 132, 0.6)",
          "rgba(54, 162, 235, 0.6)",
          "rgba(255, 206, 86, 0.6)",
          "rgba(75, 192, 192, 0.6)",
          "rgba(153, 102, 255, 0.6)",
          "rgba(255, 159, 64, 0.6)",
        ],
        borderWidth: 1,
      },
    ],
  };

  const barOptions = {
    responsive: true,
    plugins: {
      legend: { position: "top" },
    },
  };

  // ---------------------------------------------

  const pieData = {
    labels: ["Apple", "Samsung", "OnePlus"],
    datasets: [
      {
        label: "Market Share",
        data: [40, 35, 25],
        backgroundColor: [
          "rgba(255, 99, 132, 0.7)",
          "rgba(54, 162, 235, 0.7)",
          "rgba(255, 206, 86, 0.7)",
        ],
      },
    ],
  };

  const pieOptions = {
    responsive: true,
    plugins: {
      legend: { position: "bottom" },
    },
  };

  // ---------------------------------------------
  return (
    <div style={{ width: "60%", margin: "50px auto" }}>
      <h2>Bar Chart Example</h2>
      <Bar data={barData} options={barOptions} />

      <hr style={{ margin: "40px 0" }} />

      <h2>Pie Chart Example</h2>
      <Pie data={pieData} options={pieOptions} />
    </div>
  );
}

export default App;
