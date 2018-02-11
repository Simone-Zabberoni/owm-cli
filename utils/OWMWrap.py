"""
Wrapper for Argparse arguments to API call
"""

import sys
import os

import pyowm
from pyowm.exceptions import OWMError

from utils import OWMOut


def get_observation(args, function_name, *function_args):
    """
    Call the API by function_name (weather_at_place, weather_at_id etc) and return an observation object
    """
    owm = pyowm.OWM(args.key)
    try:
        observation = getattr(owm, function_name)(*function_args)
    except OWMError as err:
        print(err)
        sys.exit(2)
    return observation


def get_weather_at_place(args):
    observation = get_observation(args, 'weather_at_place', args.name)
    OWMOut.print_weather(observation, args)


def get_weather_at_id(args):
    observation = get_observation(args, 'weather_at_id', args.id)
    OWMOut.print_weather(observation, args)


def get_weather_at_coords(args):
    observation = get_observation(
        args, 'weather_at_coords', args.lat, args.lon)
    OWMOut.print_weather(observation, args)
