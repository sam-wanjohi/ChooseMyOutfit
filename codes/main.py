import requests
import config


def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{city}",
        "units": "metric",
        "APPID": api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        weather_data = response.json()
        return weather_data

    except requests.exceptions.RequestException as e:
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
            print("It might rain, You might want to bring an umbrella")
        else:
            print(
                "The heat today is roughly average. Consider wearing light clothes but take a scarf or jacket with you in case it gets colder."
            )
    else:
        print("It might be cold today. Kindly dress in warm clothing.")


if __name__ == "__main__":
    api_key = config.API_KEY
    while True:
        city = input("Enter your location (or type 'exit' to quit): ")

        if city.lower() == "exit":
            print("Exiting the weather app. Goodbye!")
            break

        weather_data = get_weather(api_key, city)

        if weather_data:
            advise_outfit(weather_data)
        else:
            print("Failed to retrieve weather data.")

