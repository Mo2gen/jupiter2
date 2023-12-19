setInterval(function() {
    updateData();
}, 600 * 1000);

function updateData() {
    $.ajax({
        url: "http://localhost:8000/update",  // Replace with the actual URL of your Django view
        type: "GET",
        dataType: "json",
        success: function(data) {
            document.getElementById('now').innerText = data.now;
            document.getElementById('weather').innerText = data.weather;
            document.getElementById('currentTemp').innerText = data.currentTemp + "°C";
            document.getElementById('humidity').innerText = data.humidity + '%';
            document.getElementById('wind').innerText = data.wind + 'km/h';
            document.getElementById('uv').innerText = data.uv;
            document.getElementById('pressure').innerText = data.pressure + 'mBar';
            document.getElementById('minmax').innerText = data.min + '/' + data.max + ' °C'
            console.log("Updated!")
        },
        error: function(xhr, status, error) {
            console.error("AJAX Request Crashed! Please sent the error to the JUpiter team!")
            console.error(xhr.responseText);
        }
    });
}