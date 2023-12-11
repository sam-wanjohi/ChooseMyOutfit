# CHOOSE MY OUTFIT APPLICATION
OVERVIEW
Choose my outfit is a command-line tool developed in Python that offers real-time weather information and outfit recommendations for a chosen city. Leveraging the OpenWeather API, the application provides users with valuable insights into the current weather conditions and suggests appropriate clothing based on the temperature and the condition.

FEATURES
Weather Information: It gives detailed weather updates, including temperature and sky condition. 
Outfit Advice: Receive personalized outfit recommendations based on the current temperature. 
Configurability: Easily configure your OpenWeather API key for seamless integration.
Interactive User Experience: User-friendly command-line interface with prompts for city selection. Clear and concise output, making it easy for users to understand the weather conditions.

Getting Started 
Prerequisites 
Before using Weather Adviser, ensure you have the following installed: Python 3.x Git (optional)

INSTALLATION
Clone the repository
git clone https://github.com/sam-wanjohi/ChooseMyOutfit.git

Navigate to the project directory
cd ChooseMyOutfit

Install dependencies
pip install -r requirements.txt

USAGE
To use the ChooseMyOutfit app, run the following command
python ChoseMyOutfit.py
Follow the prompts to choose a city, and ChooseMyOutfit will interact with the OpenWeather API to provide you with the current weather information and outfit suggestions.

HOW IT WORKS
City Selection:

Users input the name of the city for which they want to obtain weather information.
API Interaction:

The application interacts with the OpenWeather API using the provided API key.
Retrieves real-time weather data, including temperature, sky conditions, humidity, wind speed, and atmospheric pressure.
Outfit Recommendation:

Based on the temperature, the application suggests suitable clothing for the current weather conditions.
Provides advice for warm, average, or cold weather, ensuring users are prepared for the day

CONFIGURATION
ChooseMyOutfit uses the Open weather API.To configure your API key, create a file named config.py in the project root and add the following:
# config.py


