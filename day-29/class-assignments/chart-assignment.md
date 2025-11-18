### Problem 1

Create a simple bar chart using Chart.js + react-chartjs-2 inside a React project.
The chart should display monthly sales for 6 months:


| Month | Sales |
| ----- | ----- |
| Jan   | 120   |
| Feb   | 150   |
| Mar   | 170   |
| Apr   | 130   |
| May   | 190   |
| Jun   | 220   |

```javascript
// App.js (skeleton for student)
import React from "react";
import { Bar } from "react-chartjs-2";
import { Chart as ChartJS } from "chart.js";

ChartJS.register();

export default function App() {
  const data = {
    labels: [],  // TODO: Add months
    datasets: [
      {
        label: "", // TODO: Add label text
        data: [],  // TODO: Add sales data
        backgroundColor: [], // TODO: Add colors
      }
    ]
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { position: "top" },
      title: { display: true, text: "" } // TODO: Add title
    }
  };

  return (
    <div style={{ width: "60%", margin: "50px auto" }}>
      {/* TODO: Insert Bar component */}
    </div>
  );
}
```

### Problem 2

Create a pie chart using Chart.js + react-chartjs-2 that visualizes monthly expenses in 4 categories:

| Category | Amount |
| -------- | ------ |
| Food     | 5000   |
| Rent     | 12000  |
| Travel   | 3000   |
| Shopping | 4000   |

```jsx

// App.js (skeleton)
import React from "react";
import { Pie } from "react-chartjs-2";
import { Chart as ChartJS } from "chart.js";

ChartJS.register();

export default function App() {
  const data = {
    labels: [], // TODO: Add categories
    datasets: [
      {
        label: "", // TODO
        data: [],  // TODO: Add expense values
        backgroundColor: [] // TODO: Add pie slice colors
      }
    ]
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { position: "bottom" },
      title: { display: true, text: "" } // TODO: Add title
    }
  };

  return (
    <div style={{ width: "50%", margin: "50px auto" }}>
      {/* TODO: Insert Pie component */}
    </div>
  );
}

```