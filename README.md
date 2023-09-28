# seattleWeatherAPI

## Summary

Flask web app that implements APIs to return Seattle weather data. It's currently supporting 4 use cases:
1. `/get-all` that returns all data available. E.g. `curl 'http://localhost:443/get-all'`
2. `/query?date={DATE}` to query by date in `yyyy-mm-dd`. E.g. `curl 'http://localhost:443/query?date=2012-01-01'`
3. `/query?weather={WEATHER}` to query by weather. E.g. `curl 'http://localhost:443/query?weather=sun'`
4. Multi-query filtering. E.g. `curl 'http://localhost:443/query?weather=rain&limit=5'`

## Setup Guide

> Prerequisites:
> - Python3
> - Flask
> - Docker

1. Clone this git repository to your own workspace
2. Test you are able to start this flask app via: `flask run`. Make sure you're at root level of the project. You need to be able to see something similar to this (5000 is the defalt port flask uses):
  ```
  ➜  seattleWeatherAPI git:(main) ✗ flask run
   * Debug mode: off
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   * Running on http://127.0.0.1:5000
  Press CTRL+C to quit
  ```
3. Press CTRL+C to quit flask app. Start docker desktop. You need to have docker daemon running before running this app as a container
4. Build docker image. Run `docker build -t sea-weather-api-image:v0 .`
5. Run your docker image in a container. Run `docker run -p 443:8080 sea-weather-api-image:v0`. You need to be able to see something similar to this:
  ```
  ➜  seattleWeatherAPI git:(main) ✗ docker ps
  CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS          PORTS                            NAMES
  d8717ebc93de   sea-weather-api-image:v9   "python -m flask run…"   54 minutes ago   Up 54 minutes   443/tcp, 0.0.0.0:443->8080/tcp   pedantic_raman
  ```
6. Make sure the app works by running some APIs in summary section. You may also run the automated test via `python test_seattle_weather_api.py`. You should see something like this:

   ```
    ➜  seattleWeatherAPI git:(main) ✗ python test_seattle_weather_api.py
    Testing API: http://localhost:443/query
    API Response: {'data': [{'date': '2012-01-02', 'precipitation': '10.9', 'temp_max': '10.6', 'temp_min': '2.8', 'weather': 'rain', 'wind': '4.5'}, {'date': '2012-01-03', 'precipitation': '0.8', 'temp_max': '11.7', 'temp_min': '7.2', 'weather': 'rain', 'wind': '2.3'}, {'date': '2012-01-04', 'precipitation': '20.3', 'temp_max': '12.2', 'temp_min': '5.6', 'weather': 'rain', 'wind': '4.7'}, {'date': '2012-01-05', 'precipitation': '1.3', 'temp_max': '8.9', 'temp_min': '2.8', 'weather': 'rain', 'wind': '6.1'}, {'date': '2012-01-06', 'precipitation': '2.5', 'temp_max': '4.4', 'temp_min': '2.2', 'weather': 'rain', 'wind': '2.2'}]}
     test_query is successful!
    API Response: {'data': [{'date': '2012-01-08', 'precipitation': '0.0', 'temp_max': '10.0', 'temp_min': '2.8', 'weather': 'sun', 'wind': '2.0'}]}
     test_query is successful!
    Testing API: http://localhost:443/get-all
    API Response: [{'date': '2012-01-01', 'precipitation': '0.0', 'temp_max': '12.8', 'temp_min': '5.0', 'weather': 'drizzle', 'wind': '4.7'}, {'date': '2012-01-02', 'precipitation': '10.9', 'temp_max': '10.6', 'temp_min': '2.8', 'weather': 'rain', 'wind': '4.5'}, {'date': '2012-01-03', 'precipitation': '0.8', 'temp_max': '11.7', 'temp_min': '7.2', 'weather': 'rain', 'wind': '2.3'},...
    test_get_all is successful!
   ```
   
