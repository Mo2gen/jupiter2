function startfun(){
    getCoordinates()
}

function getCoordinates() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(handlecoordinates);
    }
}

function handlecoordinates(myposition) {
    console.log("Your Latitude is: " + myposition.coords.latitude)
    console.log("Your Longitude is: " + myposition.coords.longitude)
}