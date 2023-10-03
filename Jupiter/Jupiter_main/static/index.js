function getCoordinates() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showcoordinates);
    }
}

function showcoordinates(myposition) {
    console.log("Your Latitude is: " + myposition.coords.latitude)
    console.log("Your Longitude is: " + myposition.coords.longitude)
}