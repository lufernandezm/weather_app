import json
from pathlib import Path

DATA_FILE = Path("weather_data.json")

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}.")
        exit(1)

def calculate_averages(data):
    total_temp = total_humidity = 0
    for city_data in data:
        total_temp += city_data['temperature']
        total_humidity += city_data['humidity']
    avg_temp = total_temp / len(data)
    avg_humidity = total_humidity / len(data)
    return avg_temp, avg_humidity

def find_extreme_temperatures(data):
    min_temp_city = min(data, key=lambda x: x['temperature'])
    max_temp_city = max(data, key=lambda x: x['temperature'])
    return min_temp_city, max_temp_city

def print_summary(avg_temp, avg_humidity, min_temp_city, max_temp_city):
    print(f"Average Temperature: {avg_temp}")
    print(f"Average Humidity: {avg_humidity}")
    print(f"City with Lowest Temperature: {min_temp_city['city']}, Temp: {min_temp_city['temperature']} & {min_temp_city['condition']} condition")
    print(f"City with Highest Temperature: {max_temp_city['city']}, Temp: {max_temp_city['temperature']} & {max_temp_city['condition']} condition")

def main():
    data = read_json_file(DATA_FILE)
    avg_temp, avg_humidity = calculate_averages(data)
    min_temp_city, max_temp_city = find_extreme_temperatures(data)
    print_summary(avg_temp, avg_humidity, min_temp_city, max_temp_city)


if __name__ == "__main__":
    main()