# Chart.js Tutorial -- Beginner Friendly

## 1. What is Chart.js?

Chart.js is a lightweight JavaScript library for creating beautiful,
animated charts using the HTML canvas element.

### Why Use Chart.js?

-   Easy to learn
-   Supports many chart types
-   Lightweight (\~60 KB)
-   Great for dashboards and analytics

------------------------------------------------------------------------

## 2. Installation

### CDN

``` html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

### npm

``` bash
npm install chart.js
```

------------------------------------------------------------------------

## 3. Basic Chart Structure

``` html
<canvas id="myChart"></canvas>

<script>
const ctx = document.getElementById("myChart");

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['A', 'B', 'C'],
        datasets: [{
            label: 'Sample',
            data: [10, 20, 30],
            backgroundColor: ['red', 'blue', 'green']
        }]
    },
    options: {}
});
</script>
```

------------------------------------------------------------------------

## 4. Chart Components

### Type

Defines the chart type (bar, line, pie, etc.)

### Labels

X-axis labels:

``` js
labels: ['Jan', 'Feb', 'Mar']
```

### Datasets

Each dataset represents one line or bar group:

``` js
datasets: [{
  label: 'Sales',
  data: [10, 30, 50],
  backgroundColor: 'skyblue'
}]
```

### Options

Control axes, animations, tooltips, legend, and more.

------------------------------------------------------------------------

## 5. Examples

### Bar Chart

``` html
<canvas id="barChart"></canvas>
<script>
new Chart(document.getElementById("barChart"), {
  type: 'bar',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green'],
    datasets: [{
      label: 'Votes',
      data: [12, 19, 3, 5],
      backgroundColor: ['red', 'blue', 'yellow', 'green']
    }]
  },
  options: { scales: { y: { beginAtZero: true } } }
});
</script>
```

### Line Chart

``` html
<canvas id="lineChart"></canvas>
<script>
new Chart(document.getElementById("lineChart"), {
  type: 'line',
  data: {
    labels: ['Jan', 'Feb', 'Mar'],
    datasets: [{
      label: 'Sales',
      data: [100, 120, 150],
      borderColor: 'blue',
      fill: false
    }]
  }
});
</script>
```

### Pie Chart

``` html
<canvas id="pieChart"></canvas>
<script>
new Chart(document.getElementById('pieChart'), {
  type: 'pie',
  data: {
    labels: ['Chrome', 'Firefox', 'Safari'],
    datasets: [{
      data: [60, 25, 15],
      backgroundColor: ['#4285F4', '#FF7139', '#AAAAAA']
    }]
  }
});
</script>
```

------------------------------------------------------------------------

## 6. Tips

-   Keep datasets small
-   Use responsive mode
-   Destroy old charts before creating new ones in dynamic apps:

``` js
chart.destroy();
```

------------------------------------------------------------------------

## 7. Common Errors

### ctx is null

Move script to bottom of HTML or use:

``` js
window.onload = () => { ... }
```

### Chart not updating

``` js
chart.update();
```

------------------------------------------------------------------------

## Summary

-   Easy-to-use chart library
-   Multiple chart types
-   Beginner-friendly
-   Works in React, Vue, Angular, and plain JS
