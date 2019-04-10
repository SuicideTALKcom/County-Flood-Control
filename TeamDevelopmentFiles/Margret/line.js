function removeData(chart) {
  chart.data.labels.pop();
  chart.data.datasets.forEach((dataset) => {
      dataset.data.pop();
  });
  chart.update();
}

// Our labels along the x-axis
var neighborhoods = ["1 day","10 days","30 days","60 days","90+ days"];

// For drawing the lines
var Lismore_Lake = [6,0, 0, 1, 2];
var Northwest = [1, 5, 6, 10, 0];
var Lakewood = [3, 3, 1, 4, 8,];
var Riata = [10, 0,0, 0, 4];
var Saddle = [7, 8, 1, 0, 3];

var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: neighborhoods,
    datasets: [
      { 
        data: Lismore_Lake,
        label: "Lismore Lake Estates",
        borderColor: "#3e95cd",
        fill: false
      },
      { 
        data: Northwest,
        label: "Northwest Park Place",
        borderColor: "#8e5ea2",
        fill: false
      },
      { 
        data: Lakewood,
        label: "Lakewood Oaks Estates",
        borderColor: "#3cba9f",
        fill: false
      },
      { 
        data: Riata,
        label: "Riata West",
        borderColor: "#e8c3b9",
        fill: false
      },
      { 
        data: Saddle,
        label: "Saddle Ridge Estates",
        borderColor: "#c45850",
        fill: false
      }
    ]
  }
});