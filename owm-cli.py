#!/usr/bin/python

import argparse
import sys
import os

import pyowm
from pyowm.exceptions import OWMError

from utils import OWMWrap
from utils import OWMOut

# TODO: move to OWMWrap
def cityidregistry_ids_for(args):
    owm = pyowm.OWM(args.key)
    registry = owm.city_id_registry()
    ids = registry.ids_for(
        args.city_name, country=args.country, matching=args.matching)

    for item in ids:
        print("ID: {0} - {1} ({2})").format(*item)

# TODO: move to OWMWrap
def cityidregistry_locations_for(args):
    owm = pyowm.OWM(args.key)
    registry = owm.city_id_registry()

    locations = registry.locations_for(
        args.city_name, country=args.country, matching=args.matching)

    for location in locations:
        OWMOut.print_location(location)


if __name__ == '__main__':

    main_parser = argparse.ArgumentParser()

    # OWM key defaults to OWM_KEY environment variable:
    # export OWM_KEY='key_string'
    main_parser.add_argument('--key',
                             default=os.environ.get('OWM_KEY', None),
                             metavar='your_api_key')

    # Subparser foreach api
    main_subparser = main_parser.add_subparsers()

    # cityidregistry API
    cityidregistry = main_subparser.add_parser('cityidregistry')
    cityidregistry_subparser = cityidregistry.add_subparsers()

    # ids_for
    ids_for = cityidregistry_subparser.add_parser('ids_for')
    ids_for.set_defaults(func=cityidregistry_ids_for)
    ids_for.add_argument('city_name', type=str, metavar='CityName')
    ids_for.add_argument('--country', type=str,
                         default=None, metavar='Country')
    ids_for.add_argument('--matching',
                         type=str,
                         choices=['nocase', 'exact', 'like'],
                         default='nocase', metavar='MatchingCase')

    # locations_for
    locations_for = cityidregistry_subparser.add_parser('locations_for')
    locations_for.set_defaults(func=cityidregistry_locations_for)
    locations_for.add_argument('city_name', type=str, metavar='CityName')
    locations_for.add_argument(
        '--country', type=str, default=None, metavar='Country')
    locations_for.add_argument('--matching',
                               type=str,
                               choices=['nocase', 'exact', 'like'],
                               default='nocase', metavar='MatchingCase')

    # END: cityidregistry  -----------------------------------------------

    # weather API
    weather = main_subparser.add_parser('weather')
    weather_subparser = weather.add_subparsers()

    # at_place
    weather_at_place = weather_subparser.add_parser('at_place')
    weather_at_place.set_defaults(func=OWMWrap.get_weather_at_place)

    weather_at_place.add_argument(
        'name', type=str, metavar='LocationToponym')

    weather_at_place.add_argument('--to_JSON', action='store_true')
    weather_at_place.add_argument('--to_XML', action='store_true')

    # at_id
    weather_at_id = weather_subparser.add_parser('at_id')
    weather_at_id.set_defaults(func=OWMWrap.get_weather_at_id)

    weather_at_id.add_argument(
        'id', type=int, metavar='LocationID')

    weather_at_id.add_argument('--to_JSON', action='store_true')
    weather_at_id.add_argument('--to_XML', action='store_true')

    # weather_at_coords
    weather_at_coords = weather_subparser.add_parser('at_coords')
    weather_at_coords.set_defaults(func=OWMWrap.get_weather_at_coords)

    weather_at_coords.add_argument(
        'lat', type=float, metavar='Latitude')

    weather_at_coords.add_argument(
        'lon', type=float, metavar='Longitude')

    weather_at_coords.add_argument('--to_JSON', action='store_true')
    weather_at_coords.add_argument('--to_XML', action='store_true')

    # END: weather  -----------------------------------------------

    # Parse args
    args = main_parser.parse_args()

    # Check if key was provided via commandline or env variable
    # TODO: add local config file use
    if not args.key:
        exit(main_parser.print_usage())

    #print("Key: " + args.key)

    # Call the matching function
    args.func(args)
