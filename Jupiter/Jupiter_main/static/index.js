function startfun(){
    getCoordinates()
}

function getCoordinates() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(handlecoordinates);
    }
}

function handlecoordinates(myposition) {
    console.log("Latitude: " + myposition.coords.latitude)
    console.log("Longitude: " + myposition.coords.longitude)
}

function getCityCoords(cityName) {
  var geocoder = new google.maps.Geocoder();

  geocoder.geocode({ address: cityName }, function (results, status) {
    if (status === "OK") {
      if (results[0]) {
        var location = results[0].geometry.location;
        console.log("Latitude: " + location.lat());
        console.log("Longitude: " + location.lng());
      }
    }
  });
}

function getCityName(lat, lng) {
  var geocoder = new google.maps.Geocoder();
  var latlng = { lat: parseFloat(lat), lng: parseFloat(lng) };

  geocoder.geocode({ 'location': latlng }, function (results, status) {
    if (status === 'OK') {
      if (results[0]) {
        // Loop through address components to find the city
        for (var i = 0; i < results[0].address_components.length; i++) {
          var component = results[0].address_components[i];
          if (component.types.includes('locality')) {
            var cityName = component.long_name;
            console.log('City Name: ' + cityName);
            break; // Stop looping once the city name is found
          }
        }
      } else {
        console.log('No results found');
      }
    } else {
      console.log('Geocoder failed due to: ' + status);
    }
  });
}