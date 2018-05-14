import pandas as pd
import requests

PRESSURE_CONST = 7.5006e-3
APP_ID = 'b4a9d8e16b916107e741f1e84440c660'
HPASCAL_TO_PASCAL = 100
HEADERS = {
    'Cache-Control': "no-cache",
    'Postman-Token': "be7020e9-d0c8-4850-acf6-a594ccc97684"
}


def get_coordinates_by_address(address: str):
    """Returns latitude and longitude of inputted address
    if it is found; raises error otherwise.

    :param address: string to find coordinates by.
    :return: dict with "lat" and "lon" or raises error.
    """
    url = "https://nominatim.openstreetmap.org/search?"
    querystring = {
        "q": address,
        "format": "json"
    }
    response = requests.get(url, params=querystring)

    if response.text == '[]':
        raise LookupError("Can't find such address throw nominatim.")
    else:
        if len(response.json()) > 1:
            print("Found several places corresponding to the description. "
                  "The first one will be shown.")
        print('Founded place: {}'.format(response.json()[0]['display_name']))
        return {"lon": response.json()[0]['lon'],
                "lat": response.json()[0]['lat']
                }


def beautiful_print(data, title='', len_row=80, symbol='='):
    """Prints heading row before printing data.

    :param data: DataFrame to print
    :param title: header
    :param len_row: length of header row
    :param symbol: symbol to fill the row
    :return: None
    """
    print(title.center(len_row, symbol))
    print(data)
    print(symbol*len_row)


def get_current_weather_by_coordinates(lat: float,
                                       lon: float,
                                       appid=APP_ID
                                       ):
    """Beautiful prints info about current weather.

    :param lat: float -- latitude
    :param lon: float -- longitude
    :param appid: token for API
    :return: None -- all needed info is printed.
    """
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    querystring = {
        "lat": lat,
        "lon": lon,
        "appid": appid,
        "units": "metric"  # for Celsius
    }

    response = requests.get(url, headers=HEADERS, params=querystring)
    js = response.json()
    df = pd.DataFrame(
        {'description': [js['weather'][0]['description']],
         'temp,°C': [js['main']['temp']],
         'press,mm Hg': [round(js['main']['pressure'] * HPASCAL_TO_PASCAL * PRESSURE_CONST, 2)],
         'hum,%': [js['main']['humidity']],
         'wind,m/s': [js['wind']['speed']]
         },
        index=['']
    )
    return df


def get_weather_forecast_by_coordinates(lat,
                                        lon,
                                        appid=APP_ID
                                        ):
    """Beautiful prints info about forecast weather.

    :param lat: float -- latitude
    :param lon: float -- longitude
    :param appid: token for API
    :return: None -- all needed info is printed.
    """
    url = 'https://api.openweathermap.org/data/2.5/forecast?'
    querystring = {
        "lat": lat,
        "lon": lon,
        "appid": appid,
        "units": "metric"  # for Celsius
    }

    response = requests.request("GET", url, headers=HEADERS, params=querystring)

    data = response.json()['list']
    dates = [data[i]['dt_txt'][:-3] for i in range(len(data))]
    description = [data[i]['weather'][0]['description'] for i in range(len(data))]
    temperature = [data[i]['main']['temp'] for i in range(len(data))]
    pressure = [round(data[i]['main']['pressure'] * HPASCAL_TO_PASCAL * PRESSURE_CONST, 2) for i in range(len(data))]
    humidity = [data[i]['main']['humidity'] for i in range(len(data))]
    wind_speed = [data[i]['wind']['speed'] for i in range(len(data))]
    df = pd.DataFrame(
        {'description': description,
         'temp,°C': temperature,
         'press,mm Hg': pressure,
         'hum,%': humidity,
         'wind,m/s': wind_speed
         },
        index=dates)
    return df

