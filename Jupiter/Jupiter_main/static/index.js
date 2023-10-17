var lat = 0;
var long = 0;
var city = ""
async function startfun() {
  document.getElementById('location').onkeydown = function(event) {
  if (event.keyCode === 13) {
    changeCity()
  }
}
  try {
    await getCurrentCoords();
    city = await getCityName(lat, long);
    document.getElementById('location').setAttribute("placeholder", city);
  } catch (error) {
    console.error(error);
  }
}

function getCurrentCoords() {
  return new Promise((resolve, reject) => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (myposition) => {
          lat = myposition.coords.latitude;
          long = myposition.coords.longitude;
          resolve();
        },
        (error) => {
          reject(error);
        }
      );
    } else {
      reject("Geolocation is not supported.");
    }
  });
}

function getCityCoords(cityName) {
  return new Promise((resolve, reject) => {
    var geocoder = new google.maps.Geocoder();

    geocoder.geocode({ address: cityName }, function (results, status) {
      if (status === "OK") {
        if (results[0]) {
          var location = results[0].geometry.location;
          console.log("Latitude: " + location.lat());
          console.log("Longitude: " + location.lng());
          resolve();
        } else {
          reject("No results found");
        }
      } else {
        reject("Geocoder failed due to: " + status);
      }
    });
  });
}

async function getCityName(lat, lng) {
  return new Promise((resolve, reject) => {
    var geocoder = new google.maps.Geocoder();
    var latlng = { lat: parseFloat(lat), lng: parseFloat(lng) };

    geocoder.geocode({ location: latlng }, function (results, status) {
      if (status === "OK") {
        if (results[0]) {
          // Loop through address components to find the city
          for (var i = 0; i < results[0].address_components.length; i++) {
            var component = results[0].address_components[i];
            if (component.types.includes("locality")) {
              var cityName = component.long_name;
              resolve(cityName);
              break; // Stop looping once the city name is found
            }
          }
        }
      } else {
        reject("Geocoder failed due to: " + status);
      }
    });
  });
}

function changeCity(){
  console.log(document.getElementById('location').value)
  city=document.getElementById('location').value;
}