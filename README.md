# owm-cli
A Command-Line Interface to the OpenWeatherMap API



# Usage

Provide your API key via commandline:

```shell
$ ./owm-cli.py -k "your_api_key" [commands]...
```


or via environment:

```shell
$ export OWM_KEY='608fd0ea2ab29a93606e71fb6bcaf3a9'
$ ./owm-cli.py [commands]...
```


## Output samples:

Weather by toponym, the first that matches:

```shell
$ ./owm-cli.py weather at_place Ravenna 
Location: Ravenna
Coordinates: lon=12.2 lat=44.42
Observation time: 2018-02-11 21:55:00+00
Weather status: clear sky
Temperature: 1.56C
Humidity: 86%
Cloud coverage: 0%
```

Same request, JSON output:

```shell
$ ./owm-cli.py weather at_place Ravenna --to_JSON
{"status": "Clear", "visibility_distance": 10000, "clouds": 0, "temperature": {"temp_kf": null, "temp_min": 274.15, "temp": 274.71, "temp_max": 275.15}, "dewpoint": null, "humidex": null, "detailed_status": "clear sky", "reference_time": 1518386100, "weather_code": 800, "sunset_time": 1518366937, "rain": {}, "snow": {}, "pressure": {"press": 1010, "sea_level": null}, "sunrise_time": 1518329750, "heat_index": null, "weather_icon_name": "01n", "humidity": 86, "wind": {"speed": 1, "deg": 200}}
```

Weather by location id:

```shell
$ ./owm-cli.py weather at_id 5076020
Location: Ravenna
Coordinates: lon=-98.91 lat=41.03
Observation time: 2018-02-11 21:56:00+00
Weather status: clear sky
Temperature: -3.52C
Humidity: 46%
Cloud coverage: 1%
```

Weather by coordinates:

```shell
$ ./owm-cli.py weather at_coords 44.42 12.6
Location: Cervia
Coordinates: lon=12.6 lat=44.42
Observation time: 2018-02-11 21:55:00+00
Weather status: clear sky
Temperature: 1.54C
Humidity: 100%
Cloud coverage: 0%
```


Get IDs for a toponym:

```shell
$ ./owm-cli.py cityidregistry ids_for Ravenna
ID: 3169561 - Ravenna (IT)
ID: 5006818 - Ravenna (US)
ID: 5076020 - Ravenna (US)
ID: 5167737 - Ravenna (US)
ID: 6540121 - Ravenna (IT)
```

Get locations and details for a toponym:

```shell
$ ./owm-cli.py cityidregistry locations_for Ravenna
ID: 3169561 - Ravenna (IT) - lon=12.20111 lat=44.4175
ID: 5006818 - Ravenna (US) - lon=-85.936989 lat=43.189468
ID: 5076020 - Ravenna (US) - lon=-98.912582 lat=41.026119
ID: 5167737 - Ravenna (US) - lon=-81.24205 lat=41.157558
ID: 6540121 - Ravenna (IT) - lon=12.19873 lat=44.416969
```




