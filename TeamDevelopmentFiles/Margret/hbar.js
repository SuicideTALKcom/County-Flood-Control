new Chart(document.getElementById("bar-chart"), {
    type: 'horizontalBar',
    data: {
      labels: ["Lismore Lake Estates", "Northwest Park Place", "Lakewood Oaks Estates", "Riata West", "Saddle Ridge Estates"],
      datasets: [
        {
          label: "Number of Homes for Sale",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
          data: [5,8,8,10,7]
        }
      ]
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: 'This is dummy data'
      }
    }
});