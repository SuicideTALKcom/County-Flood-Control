// Creating map object
var map = L.map("map", {
  center: [29.946408, -95.565155],
  zoom: 12
});


// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(map);

//Lismore Lake Estates Neighborhood
L.polygon([
  [29.973089, -95.613632],
  [29.969535, -95.609346],
  [29.968503, -95.610870],
  [29.970947, -95.616149]
], {
  color: "blue",
  fillColor: "blue",
  fillOpacity: 0.75
}).addTo(map);

L.circle([29.970342, -95.613021], {radius: 1500}).addTo(map);


//Northwest Park Place Neighborhood
L.polygon([
  [29.934775, -95.497663],
  [29.934978, -95.481665],
  [29.919636, -95.481742],
  [29.925848, -95.497835]
], {
  color: "red",
  fillColor: "red",
  fillOpacity: 0.75
}).addTo(map);

L.circle([29.929307, -95.488264], {radius: 1500}).addTo(map);

//Lakewood Oaks Estates Neighborhood
L.polygon([
  [30.004304, -95.635300],
  [30.006088, -95.623831],
  [29.999519, -95.629035]
], {
  color: "green",
  fillColor: "green",
  fillOpacity: 0.75
}).addTo(map);

L.circle([30.003561, -95.628820], {radius: 1500}).addTo(map);

//Riata West Neighborhood
L.polygon([
  [29.942208, -95.686817],
  [29.941427, -95.679725],
  [29.936063, -95.686634]
], {
  color: "orange",
  fillColor: "orange",
  fillOpacity: 0.75
}).addTo(map);

L.circle([29.940409, -95.683775], {radius: 1500}).addTo(map);

//Saddle Ridge Estates Neighborhood
L.polygon([
  [30.029387, -95.743263],
  [30.029944, -95.738231],
  [30.012779, -95.737865],
  [30.012795, -95.742788]
], {
  color: "purple",
  fillColor: "purple",
  fillOpacity: 0.75
}).addTo(map);

L.circle([30.021231, -95.740517], {radius: 1500}).addTo(map);



// // var link = "http://data.beta.nyc//dataset/0ff93d2d-90ba-457c-9f7e-39e47bf2ac5f/resource/" +
// // "35dd04fb-81b3-479b-a074-a27a37888ce7/download/d085e2f8d0b54d4590b1e7d1f35594c1pediacitiesnycneighborhoods.geojson";

// // Function that will determine the color of a neighborhood based on the borough it belongs to
// function chooseColor(borough) {
//   switch (borough) {
//   case "Brooklyn":
//     return "yellow";
//   case "Bronx":
//     return "red";
//   case "Manhattan":
//     return "orange";
//   case "Queens":
//     return "green";
//   case "Staten Island":
//     return "purple";
//   default:
//     return "black";
//   }
// }

// // Grabbing our GeoJSON data..
// d3.json(link, function(data) {
//   // Creating a geoJSON layer with the retrieved data
//   L.geoJson(data, {
//     // Style each feature (in this case a neighborhood)
//     style: function(feature) {
//       return {
//         color: "white",
//         // Call the chooseColor function to decide which color to color our neighborhood (color based on borough)
//         fillColor: chooseColor(feature.properties.borough),
//         fillOpacity: 0.5,
//         weight: 1.5
//       };
//     },
//     // Called on each feature
//     onEachFeature: function(feature, layer) {
//       // Set mouse events to change map styling
//       layer.on({
//         // When a user's mouse touches a map feature, the mouseover event calls this function, that feature's opacity changes to 90% so that it stands out
//         mouseover: function(event) {
//           layer = event.target;
//           layer.setStyle({
//             fillOpacity: 0.9
//           });
//         },
//         // When the cursor no longer hovers over a map feature - when the mouseout event occurs - the feature's opacity reverts back to 50%
//         mouseout: function(event) {
//           layer = event.target;
//           layer.setStyle({
//             fillOpacity: 0.5
//           });
//         },
//         // When a feature (neighborhood) is clicked, it is enlarged to fit the screen
//         click: function(event) {
//           map.fitBounds(event.target.getBounds());
//         }
//       });
//       // Giving each feature a pop-up with information pertinent to it
//       layer.bindPopup("<h1>" + feature.properties.neighborhood + "</h1> <hr> <h2>" + feature.properties.borough + "</h2>");

//     }
//   }).addTo(map);
// });
