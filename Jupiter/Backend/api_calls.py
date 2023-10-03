"""
Fabio Di Grillo
03.10.2023
"""


import requests

# Wichtig! Ohne diesen wird kein Zugirff erlaubt
apiKey = "C6KzQwff39MA8kV1"

def get_forecast (apikey,lat_long):
    return requests.get(f"https://api.pirateweather.net/forecast//")





print(get_forecast(apiKey))