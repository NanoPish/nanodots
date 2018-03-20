#!/usr/bin/env python
import pyowm

owm = pyowm.OWM('2505ce29adcf3f3d6caf15b18e617417')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('Paris,FR')
w = observation.get_weather()

# Weather details
#print (w.get_wind())                  # {'speed': 4.6, 'deg': 330}
#print (w.get_humidity())              # 87
#print (w.get_temperature('celsius').)  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

current_temp = w.get_temperature('celsius')
output = current_temp["temp"]
print (str(output))
