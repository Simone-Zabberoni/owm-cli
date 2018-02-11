"""
Module for command line output
"""

import sys
import os

import pyowm
from pyowm.exceptions import OWMError


def print_weather(observation, args):
    weather = observation.get_weather()
    location = observation.get_location()

    if args.to_JSON:
        print(weather.to_JSON())
        sys.exit(0)

    if args.to_XML:
        print(weather.to_XML())
        sys.exit(0)

    print('Location: ' + location.get_name())
    print('Coordinates: lon=' + str(location.get_lon()) +
          ' lat=' + str(location.get_lat()))
    print('Observation time: ' + weather.get_reference_time(timeformat='iso'))
    print('Weather status: ' + weather.get_detailed_status())
    print('Temperature: ' +
          str(weather.get_temperature('celsius')['temp']) + 'C')
    print('Humidity: ' + str(weather.get_humidity()) + '%')
    print('Cloud coverage: ' + str(weather.get_clouds()) + '%')


def print_location(location):
    print('ID: ' + str(location.get_ID()) +
          ' - ' + location.get_name() +
          ' (' + location.get_country() + ') - ' +
          'lon=' + str(location.get_lon()) + ' lat=' + str(location.get_lat())
          )




