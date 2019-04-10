// function clearBox(elementID){
//     document.getElementById("hbar-chart").innerHTML = "";
// }
// return(clearBox);

// function renderBar(){
// clearBox()

// d3.csv("data.csv", function(error, data) {
// 	data.forEach(function(d) {
// 		d.date = parseDate(d.date);
// 		d.close = +d.close;
// });


// d3.json('/api/neighborhood', defaults={'neighborhood':True})
//     .then(function (datahomes) {
        // var neighborhood = datahomes.Neighbhorhood
        // var address = datahomes.Address
        // var price = datahomes.Price
        // var days = datahomes.Days_on_Market
        // var agent = datahomes.Agent


    //     console.log(datahomes);
    // });

    d3.json("/api/neighborhood").then(function(data){
        // data.forEach(function(d){
        //     d.Neighborhood = d.Neighborhood;
        //     d.Agent = d.Agent;
        //     d.Price = d.Price;
        //     d.Days_on_Market= d.Days_on_Market;
        //     d.Address = d.Address;
        // })
    
        let homesObject = {}
    
        data.forEach((home)=>{
            if (!homesObject[home.Neighborhood]) homesObject[home.Neighborhood] = []
            homesObject[home.Neighborhood].push(home)
        })
        console.log(homesObject, typeof homesObject);
        numberHomes = Object.values(homesObject).map((hood)=> hood.length);
        neighborhoodNames = Object.keys(homesObject);
    
        hbar(neighborhoodNames, numberHomes)
    })
    
    function hbar(namesArray, homeNumberArray){
        console.log(namesArray, homeNumberArray)
    return new Chart(document.getElementById("hbar-chart"), {
        type: 'horizontalBar',
        data: {
            labels: namesArray,
            datasets: [
                {
                    label: "Number of Homes for Sale",
                    backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
                    data: homeNumberArray
                }
            ]
        },
        options: {
            legend: { display: false },
            title: {
                display: true,
                // text: 'Total Number of Homes for Sale by Neighbohood'
            },
            scales: {
                xAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        },
    });
    }
    
    // clearBox("hbar-chart")
    
    // function clear()
    //     var chart = document.getElementById("hbar-chart").getContext("2d");
    //     chart.destroy();
    
    // return(clear);
    function barchart(){
    return new Chart(document.getElementById("bar-chart"), {
        type: 'bar',
        data: {
            labels: ["Lismore Lake Estates", "Northwest Park Place", "Lakewood Oaks Estates", "Riata West", "Saddle Ridge Estates"],
            datasets: [
                {
                    label: "Cost",
                    backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
                    data: [969700, 729990, 3058000, 1721498, 10404500]
                }
            ]
        },
        options: {
            legend: { display: false },
            title: {
                display: true,
                // text: 'Total Buyout Amount per Neighbohood of Available Listings'
            },
            layout: {
                padding: {
                    left: 50,
                    right: 0,
                    top: 0,
                    bottom: 0
                }
            }
        }
    });
}
    
    // // Our labels along the x-axis
    // var neighborhoods = ["1 day", "10 days", "30 days", "60 days", "90+ days"];
    
    // // For drawing the lines
    // var Lismore_Lake = home_details
    // var Northwest = [1, 5, 6, 10, 0];
    // var Lakewood = [3, 3, 1, 4, 8,];
    // var Riata = [10, 0, 0, 0, 4];
    // var Saddle = [7, 8, 1, 0, 3];
    function linechart(){
    return new Chart(document.getElementById("linechart"), {
        type: 'line',
        data: {
            labels: ["1+ day", "10+ days", "30+ days", "60+ days", "90+ days"],
            datasets: [
                {
                    data: [0, 0, 2, 0, 1],
                    label: "Lismore Lake Estates",
                    borderColor: "#3e95cd",
                    fill: false
                },
                {
                    data: [2, 1, 1, 0, 0],
                    label: "Northwest Park Place",
                    borderColor: "#8e5ea2",
                    fill: false
                },
                {
                    data: [1, 2, 1, 0, 2],
                    label: "Lakewood Oaks Estates",
                    borderColor: "#3cba9f",
                    fill: false
                },
                {
                    data: [3, 3, 0, 1, 1],
                    label: "Riata West",
                    borderColor: "#e8c3b9",
                    fill: false
                },
                {
                    data: [0, 2, 0, 0, 3],
                    label: "Saddle Ridge Estates",
                    borderColor: "#c45850",
                    fill: false
                }
            ]
        }
    });
}
 linechart()
 barchart()   
    
    
    
    // return (renderBar);
    