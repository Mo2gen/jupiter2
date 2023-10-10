function startfun(){
    getCoordinates()
}

function getCoordinates() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(handlecoordinates);
    }
}

function handlecoordinates(myposition) {
    // hier get request schicken
}

function geocodeCity(cityName) {
  var geocoder = new google.maps.Geocoder();

  geocoder.geocode({ address: cityName }, function (results, status) {
    if (status === "OK") {
      if (results[0]) {
        var location = results[0].geometry.location;
        console.log("Latitude: " + location.lat());
        console.log("Longitude: " + location.lng());
      } else {
        console.log("No results found");
      }
    } else {
      console.log("Geocode was not successful for the following reason: " + status);
    }
  });
}