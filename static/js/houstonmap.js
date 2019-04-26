// Creating map object
var map = L.map("map", {
  center: [29.961274, -95.632013],
  zoom: 9.5
});

//For next project, create table that holds the coordinates instead of storing in this JS file 
//This will remove having to update when new neighborhoods are needed to be searched


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

var lismore = L.circle([29.970342, -95.613021], {radius: 1500}).addTo(map);

lismore.bindPopup("<h1>"+"Lismore Lake Estates"+"</h1> <hr>"+ "12151 Lismore Lake Drive, $329900, 45 days" + "<br>" + "12035 Lismore Lake Drive, $349900, 56 days" + "<br>" + "11918 Galentine Point, $289900, 176 days");

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

var northwest = L.circle([29.929307, -95.488264], {radius: 1500}).addTo(map);
northwest.bindPopup("<h1>"+"NorthWest Park Place"+"</h1> <hr>"+ "5822 Wickover Lane, $169990, 5 days" + "<br>" + "10110 Fallmont Court, $170000, 8 days" + "<br>" + "9827 Golden Prairie Lane, $195000, 11 days" + "<br>" + "6035 Cascadera Drive, $195000, 35 days");

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

var lakewood = L.circle([30.003561, -95.628820], {radius: 1500}).addTo(map);

lakewood.bindPopup("<h1>"+"Lakewood Oaks Estates"+"</h1> <hr>"+ "13910 Springmint Drive, $615000, 5 days" + "<br>" + "13618 Pegasus Road, $450000, 10 days" + "<br>" + "13718 Pegasus Road, $529000, 24 days" + "<br>" + "13511 Pegasus Road, $499500, 30 days" + "<br>" + "13106 Springmint Court, $499500, 116 days" + "<br>" + "14011 Pegasus Circle, $465000, 214 days");

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

var riata = L.circle([29.940409, -95.683775], {radius: 1500}).addTo(map);

// Giving each feature a pop-up with information pertinent to it
riata.bindPopup("<h1>"+"Riata West"+"</h1> <hr>"+ "11115 Riata Canyon Drive, $179900, 1 days" + "<br>" + "10902 Barker View Drive, $224900, 2 days" + "<br>" + "10915 Barker View Drive, $179999, 4 days" + "<br>" + "17951 Branch Creek Drive, $198500, 13 days" + "<br>" + "10923 Barker View Drive, $225000, 19 days" + "<br>" + "17923 Cypress Side Drive, $224500, 27 days" + "<br>" + "18030 Riata Crossing Drive, $189900, 80 days" + "<br>" + "11207 Barker West Drive, $298799, 130 days");


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

var saddle = L.circle([30.021231, -95.740517], {radius: 1500}).addTo(map);

saddle.bindPopup("<h1>"+"Saddle Ridge Estates"+"</h1> <hr>"+ "16810 Saddle Ridge Pass, $4999500, 17 days" + "<br>" + "16703 Saddle Ridge Pass, $1258000, 27 days" + "<br>" + "16510 Saddle Ridge Pass, $1997000, 134 days" + "<br>" + "17203 Saddle Ridge Pass, $2150000, 165 days");

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
