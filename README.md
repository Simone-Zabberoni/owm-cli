# owm-cli
A Command-Line Interface to the OpenWeatherMap API



# Usage

Provide your API key via commandline:

```shell
$ ./owm-cli.py --key "your_api_key" [commands]...
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


# Docker support

Build from Dockerfile:

```shell
~/Dev/owm-cli$ cd scripts/
~/Dev/owm-cli/scripts$ ./build_docker.sh 
Sending build context to Docker daemon  123.9kB
Step 1/7 : FROM alpine:3.7
 ---> e21c333399e0
Step 2/7 : MAINTAINER Simone Zabberoni <simone.zabberoni@gmail.com>
 ---> Using cache
 ---> ddd9085f8dc4
Step 3/7 : RUN apk add --update python3 py-pip
 ---> Using cache
 ---> 8f7064f6358e
Step 4/7 : RUN pip install pyowm
 ---> Using cache
 ---> d93e1402fbdd
Step 5/7 : ADD . /pyowm
 ---> Using cache
 ---> 5e139ad1a9d4
Step 6/7 : WORKDIR /pyowm
 ---> Using cache
 ---> 51f4449e48e4
Step 7/7 : ENTRYPOINT ["/pyowm/owm-cli.py"]
 ---> Using cache
 ---> 61f9b03e87ef
Successfully built 61f9b03e87ef
Successfully tagged owmcli:latest
```


Docker run with OWM_KEY environmental variable:


```shell
$ docker run -e OWM_KEY pyowm-cli weather at_place Roma
Location: Rome
Coordinates: lon=12.48 lat=41.89
Observation time: 2018-02-11 22:55:00+00
Weather status: clear sky
Temperature: 3.33C
Humidity: 69%
Cloud coverage: 0%
```


Aliasing:

```shell
$ alias pyowm-cli="docker run -e OWM_KEY pyowm-cli"

$ pyowm-cli weather at_place Helsinki
Location: Helsinki
Coordinates: lon=24.94 lat=60.17
Observation time: 2018-02-11 22:50:00+00
Weather status: light snow
Temperature: -4.0C
Humidity: 92%
Cloud coverage: 75%
```





