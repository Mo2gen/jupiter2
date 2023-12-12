var lat = 0;
var long = 0;
var city = ""
var date = ""
async function startfun() {
    document.getElementById('location').onkeydown = async function (event) {
        if (event.key === "Enter" || event.keyCode === 13) {
            changeCity();
            const cityCoords = await getCityCoords(city);
            lat = cityCoords.lat()
            long = cityCoords.lng()
            setCookie(lat, long)
        }
    }
    document.getElementById('date').onchange = function () {
        date = document.getElementById('date').value
        setCookie(lat, long, date)
        console.log('datum geändert!' + date)
    };
    try {
        if (document.cookie.split('; ')[2] == undefined) {
            await getCurrentCoords();
            city = await getCityName(lat, long);
            await setCookie(lat, long);
            ({ long, lat, date } = readCookies());
        }
        else {
            ({ long, lat, date } = readCookies());
            city = await getCityName(lat, long);
        }
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
          // Pass the coordinates to the resolve function
          resolve(location);
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

function setCookie(lat, long, date="not set") {
    document.cookie = "lat=" + lat;
    document.cookie = "long=" + long;
    if(date === "not set"){
        if(document.getElementById('date').value !== ''){
        document.cookie = "date=" + document.getElementById('date').value
        }
        else{
            document.cookie = "date=" + new Date().toISOString().split('T')[0];
        }
    }
    else {
        document.cookie = "date=" + date
    }
}