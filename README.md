# Weather App Agregator 

The Weather Data Aggregator is a command-line application designed to process weather data from a static JSON file. It aggregates information on temperatures, humidity, and conditions across various cities, providing a concise summary of average values and extremes.

## Requirements
- Python 3.x
- A JSON file named weather_data.json located in the same directory as the application scripts.

The JSON file should follow this structure:
```bash
[
  {
    "city": "City Name",
    "temperature": 25,
    "humidity": 80,
    "condition": "Sunny"
  },
  ...
]
```

## How to Run

- Ensure Python 3.x is installed on your system.
- Place your weather_data.json file in the same directory as the application scripts.
- Navigate to the directory containing the application scripts.
- Run the command 

    #### ` python main.py.`

## Expected Output

The application will output a summary similar to the following in your console:

```bash
Average Temperature: XX.X
Average Humidity: YY.Y
City with Lowest Temperature: City Name, Temp: ZZ & [Condition] condition
City with Highest Temperature: City Name, Temp: AA & [Condition] condition
```
