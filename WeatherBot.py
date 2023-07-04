import discord #import discord library
import requests#import requests library

#initializes a new instance of the discord.Client class with default intents.
#The discord.Intents.default() method sets the default intents for the client instance. 
client = discord.Client(intents = discord.Intents.default())

#Add discord token to connect with my bot. 
token='MTA5Mzc3ODUwMzk2NDU2NTU4Ng.GVzZA8.qFsUlwfEw5CN-JyqtWhliJsXP_e5JRlKgkcvlM'

# register an event handler function as client.event
@client.event
async def on_ready():#event is triggered when the bot has successfully connected to the Discord API and is ready to receive and send messages.
    print('Bot is ready')#printing that bot is ready to use.

@client.event
async def on_message(message):#getting users input as message. 
    
    if message.content.startswith('!weather-'):#Check wheather the input insert in correct syntex or not.
        city = message.content[9:]#store the city name given my user in city.
        try:
           
            #weatherapi kye
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=15c721f583caba8b3143a915c59d4299')
            data = response.json()#storing result of weather in data
            temp = round(data['main']['temp'] - 273.15, 2)#storing city tempreture in temp
            feels_like = round(data['main']['feels_like'] - 273.15, 2)#storing city feels like in feels_like
            humidity = data['main']['humidity']#storing city humidity in humidity.
            wind_speed = data['wind']['speed']#storing city wind speed in wind_speed.
            weather_desc = data['weather'][0]['description']#storing city description in weather_desc.
            city_name = data['name']#storing city name in city_name
            country_code = data['sys']['country'] # storing country  code in country_code.
            
            #printing the result to the user. 
            await message.channel.send(f'Temperature in {city_name}, {country_code} is {temp}°C. \n It feels like {feels_like}°C. \n Humidity is {humidity}%. \n Wind speed is {wind_speed} m/s. {weather_desc}.')
            
        except:# condition for wrong syntax
            await message.channel.send('City not found')# printing city not found.
   
    elif message.content.startswith('!w-'):#another true condition.
        city = message.content[3:]#storing city name in city.
        try:
            #weatherapi kye
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=15c721f583caba8b3143a915c59d4299')
           
            data = response.json()#storing result of weather in data
            temp = round(data['main']['temp'] - 273.15, 2)#storing city tempreture in temp
            feels_like = round(data['main']['feels_like'] - 273.15, 2)#storing city feels like in feels_like
            humidity = data['main']['humidity']#storing city humidity in humidity.
            wind_speed = data['wind']['speed']#storing city wind speed in wind_speed.
            weather_desc = data['weather'][0]['description']#storing city description in weather_desc.
            city_name = data['name']#storing city name in city_name.
            country_code = data['sys']['country']# storing country  code in country_code.
           
            await message.channel.send(f'Temperature in {city_name}, {country_code} is {temp}°C. \n It feels like {feels_like}°C. \n Humidity is {humidity}%. \n Wind speed is {wind_speed} m/s. {weather_desc}.')
        
        except:# condition for wrong syntax
            await message.channel.send('City not found')# printing city not found.
   
    elif message.content.startswith('!weather?') or message.content.startswith('!w?'):#condition if user needs a guid.
        await message.channel.send('To get the weather information of a city, type "!weather-" or "!w-" followed by the city name. For example, "!weather-tokyo" or "!w-Toronto"')#printing guid to user.
    
    
client.run(token)# run the discord token.
