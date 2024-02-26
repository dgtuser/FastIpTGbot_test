import requests

key = r"804c97b061374c55b9583509240102"

def getForecast(city: str, days: int):
    weatherForecast = {}

    params = {
        "key": key,
        "q": city,
        "days": days
    }

    response = requests.get("https://api.weatherapi.com/v1/forecast.json", params=params)

    for i in range(days):
        tempDict, tempDay = {}, response.json()['forecast']['forecastday'][i]

        tempForecast = tempDay['day']
        
        tempDict['day'] = tempDay['date']
        tempDict['avgTemp'] = tempForecast['avgtemp_c']
        tempDict['minTemp'] = tempForecast['mintemp_c']
        tempDict['maxTemp'] = tempForecast['maxtemp_c']

        weatherForecast[("Forecast for day {0}").format(i + 1)] = tempDict.items()

    return weatherForecast
    # return response.json()['forecast']['forecastday'][0]  