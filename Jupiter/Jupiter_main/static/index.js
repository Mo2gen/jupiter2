var lat = 0;
var long = 0;
var city = ""
var date = ""
async function startfun() {
    document.getElementById('location').onkeydown = function (event) {
        if (event.key === "Enter" || event.keyCode === 13) {
            changeCity();
            getCityCoords(city);
        }
    }
    try {
        await getCurrentCoords();
        city = await getCityName(lat, long);
        await setCookie(lat, long);  // Ensure this is called after reading cookies
        lat, long, date = readCookies();
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
  if (document.getElementById('location').value!== ""){
    city=document.getElementById('location').value;
    document.getElementById('location').setAttribute("placeholder", city);
  }
}

function readCookies() {
    var cookies = document.cookie.split('; ');

    var long, lat, date;

    cookies.forEach(function(cookie) {
        var parts = cookie.split('=');
        var name = parts[0];
        var value = parts[1];

        if (name == 'long') {
            long = parseFloat(value);  // Assuming long is a floating-point number
        } else if (name == 'lat') {
            lat = parseFloat(value);   // Assuming lat is a floating-point number
        } else if (name == 'date') {
            date = value;  // Assuming date is a string
        }
    });

    return {
        long: long,
        lat: lat,
        date: date
    };
}

function setCookie(lat, long) {
    document.cookie = "lat=" + lat;
    document.cookie = "long=" + long;
    if(document.getElementById('date').value !== ''){
        console.log('AAAAAAAAA')
        document.cookie = "date=" + document.getElementById('date').value
    }
    else{
        console.log('BBBBBBBBBBBBBB')
        document.cookie = "date=" + new Date().toISOString().split('T')[0];
    }
}