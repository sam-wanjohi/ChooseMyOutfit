import requests
import config
# import config file which contains apikey for security of the key

def get_weather(api_key, host, location):
    """
    Retrieves weather data for a specific location.

    :param api_key: The API key for accessing the weather API. (str)
    :param host: The host for accessing the weather API. (str)
    :param location: The location for which to retrieve weather data. (str)

    :return: The weather data for the specified location. Returns None if an error occurs. (dict or None)
    """
    base_url = f"https://open-weather13.p.rapidapi.com/city/{location}"
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": host
    }
    params = {"q": location, "units": "metric"}

    try:
        response = requests.get(base_url, headers=headers, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            error_message = data.get('sorry! An error occurred.', 'Unknown error')
            print(f"Error: {error_message}")
            return None

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def advise_outfit(weather):
    """
    Generates an outfit advice based on the weather.

    Args:
        weather (dict): A dictionary containing weather information.
    return:
        An outfit message according to the weather condition of a chosen city
    """
    if "main" not in weather or "temp" not in weather["main"]:
        print("Error: Unable to retrieve weather information.")
        return

    heat = weather["main"]["temp"]
    conditions = weather.get("weather", [{"description": "N/A"}])[0]["description"]

    print(f"Current temperature: {heat}°C")
    print(f"Sky: {conditions}")

    if heat > 24:
        print("It's quite warm today! Light clothing would be great.")
    elif 14 <= heat <= 24:
        if "rain" in conditions.lower():
            print("You might want to bring an umbrella")
        else:
            print(
                "The heat today is roughly average. Consider wearing light clothes but take a scarf or jacket with you in case it gets colder."
            )
    else:
        print("It might be cold today. Kindly dress in warm clothing.")

if __name__ == "__main__":
    api_key = config.API_KEY
    host = "open-weather13.p.rapidapi.com"
    location = input("Choose your city: ")

    weather_data = get_weather(api_key, host, location)

    if weather_data:
        advise_outfit(weather_data)

