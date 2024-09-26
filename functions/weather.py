<<<<<<< HEAD
import requests
import datetime as dt
import os

def get_weather_updates(city):
    API_KEY = '9a718f69e5786c9dc14d6a051dc4e878'  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()  

    city_name = data['name']
    temperature = data['main']['temp']
    temperature_min= data['main']['temp_min']
    temperature_max= data['main']['temp_max']
    temperature_feels_like= data['main']['feels_like']
    weather_desc = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    sunrise_time = dt.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
    sunset_time = dt.datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')

    weather_paragraph=(f"The weather in {city_name} is currently {weather_desc}. The temperature is {temperature}°C, "
                    f"feeling like {temperature_feels_like}°C. The minimum temperature today is {temperature_min}°C, "
                    f"with a maximum of {temperature_max}°C. Humidity is at {humidity}%, and wind speed is {wind_speed} m/s. "
                    f"Sunrise occurred at {sunrise_time}, and sunset is expected at {sunset_time}.")

    # output_directory = 'C:/Users/91965/SSST/chatbot using gemini flash- multiple pdf files/project/data'  # Change this to your desired path
    # os.makedirs(output_directory, exist_ok=True)

    # file_path = os.path.join(output_directory,f'{city}_weather.txt')
    
    # with open(file_path, 'w') as textfile:
    #     textfile.write(weather_paragraph)
    return weather_paragraph




=======
import requests
import datetime as dt
import os

def get_weather_updates(city):
    API_KEY = '9a718f69e5786c9dc14d6a051dc4e878'  
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()  

    city_name = data['name']
    temperature = data['main']['temp']
    temperature_min= data['main']['temp_min']
    temperature_max= data['main']['temp_max']
    temperature_feels_like= data['main']['feels_like']
    weather_desc = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    sunrise_time = dt.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
    sunset_time = dt.datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')

    weather_paragraph=(f"The weather in {city_name} is currently {weather_desc}. The temperature is {temperature}°C, "
                    f"feeling like {temperature_feels_like}°C. The minimum temperature today is {temperature_min}°C, "
                    f"with a maximum of {temperature_max}°C. Humidity is at {humidity}%, and wind speed is {wind_speed} m/s. "
                    f"Sunrise occurred at {sunrise_time}, and sunset is expected at {sunset_time}.")

    # output_directory = 'C:/Users/91965/SSST/chatbot using gemini flash- multiple pdf files/project/data'  # Change this to your desired path
    # os.makedirs(output_directory, exist_ok=True)

    # file_path = os.path.join(output_directory,f'{city}_weather.txt')
    
    # with open(file_path, 'w') as textfile:
    #     textfile.write(weather_paragraph)
    return weather_paragraph




>>>>>>> 4789a245e1253bccb4d410a3f6be10f05e2588c3
