from requests import get
from constants import OWM_TOKEN

def get_weather_ru(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_TOKEN}&units=metric&lang=ru"
        response = get(url)
        data = response.json()

        temp = data["main"]["temp"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind = data["wind"]["speed"]
        pressure = round(data["main"]["pressure"] * 0.750064)    # гектопаскаль —> мм. рт. ст. 
        country = data["sys"]["country"]
  
        weatherMessage = f"🌤️ Погода для города <b>{city}</b> ({country}):\n\n"
        weatherMessage += "================================\n"
        weatherMessage += f"🌡️ Температура:\n"
        weatherMessage += f"        • <b><i>Текущая: {temp}°C</i></b>\n"
        weatherMessage += f"        • Минимальная: {temp_min}°C\n"
        weatherMessage += f"        • Максимальная: {temp_max}°C\n"
        weatherMessage += f"👍 Ощущается как: {feels_like}°C\n"
        weatherMessage += "================================\n\n"
        weatherMessage += f"🗜 Давление: {pressure} мм. рт. ст.\n"
        weatherMessage += f"💨 Ветер: {wind} м/с\n"
        weatherMessage += f"💧 Влажность: {humidity}%\n"
        weatherMessage += f"🌧️ Описание: {condition}"

        return weatherMessage

    except:
        return "⛔ Такого города не существует ⛔"
    
def get_weather_en(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OWM_TOKEN}&units=metric&lang=en"
        response = get(url)
        data = response.json()

        temp = data["main"]["temp"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind = data["wind"]["speed"]
        pressure = data["main"]["pressure"]
        country = data["sys"]["country"]
  
        weatherMessage = f"🌤️ Weather in <b>{city}</b> ({country}):\n\n"
        weatherMessage += "================================\n"
        weatherMessage += f"🌡️ Temperature:\n"
        weatherMessage += f"        • <b><i>Current: {temp}°C</i></b>\n"
        weatherMessage += f"        • Min: {temp_min}°C\n"
        weatherMessage += f"        • Max: {temp_max}°C\n"
        weatherMessage += f"👍 Feels like: {feels_like}°C\n"
        weatherMessage += "================================\n\n"
        weatherMessage += f"🗜 Pressure: {pressure} hPa\n"
        weatherMessage += f"💨 Wind: {wind} meter/sec\n"
        weatherMessage += f"💧 Humidity: {humidity}%\n"
        weatherMessage += f"🌧️ Description: {condition}"

        return weatherMessage

    except:
        return "⛔ There is no such city you entered! ⛔"