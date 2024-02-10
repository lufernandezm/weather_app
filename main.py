import sys
import json
from pathlib import Path
from colorama import Fore, Style

class CityWeather:
    def __init__(self, city_data):
        try:
            self.city = city_data['city']
            self.temperature = city_data['temperature']
            self.humidity = city_data['humidity']
            self.condition = city_data['condition']
        except KeyError as e:
            handle_error(f"Invalid data format. '{e.args[0]}' key not found.")

def handle_error(message):
    print(message)
    exit(1)

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [CityWeather(city_data) for city_data in json.load(file)]
    except FileNotFoundError:
        handle_error(f"Error: {file_path} not found.")
    except json.JSONDecodeError:
        handle_error(f"Error decoding JSON from {file_path}.")

def calculate_averages(data):
    try:
        total_temp = sum(city.temperature for city in data)
        total_humidity = sum(city.humidity for city in data)
        avg_temp = total_temp / len(data)
        avg_humidity = total_humidity / len(data)
        return avg_temp, avg_humidity
    except ZeroDivisionError:
        handle_error("Error: No data to calculate averages.")

def find_extreme_temperatures(data):
    min_temp_city = min(data, key=lambda x: x.temperature)
    max_temp_city = max(data, key=lambda x: x.temperature)
    return min_temp_city, max_temp_city

def print_summary(avg_temp, avg_humidity, min_temp_city, max_temp_city):
    print(Fore.CYAN + "\nWeather Data Summary:")
    print("---------------------")
    print(Fore.GREEN + f"Average Temperature: {avg_temp:.2f} degrees C")
    print(f"Average Humidity: {avg_humidity:.2f}%")
    print(Fore.YELLOW + "\nCity with Lowest Temperature:")
    print(Fore.WHITE + f"City: {min_temp_city.city}")
    print(f"Temperature: {min_temp_city.temperature} degrees C")
    print(f"Condition: {min_temp_city.condition}")
    print(Fore.YELLOW + "\nCity with Highest Temperature:")
    print(Fore.WHITE + f"City: {max_temp_city.city}")
    print(f"Temperature: {max_temp_city.temperature} degrees C")
    print(f"Condition: {max_temp_city.condition}")
    print(Style.RESET_ALL)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_json_file>")
        exit(1)

    data_file = Path(sys.argv[1])
    data = read_json_file(data_file)
    avg_temp, avg_humidity = calculate_averages(data)
    min_temp_city, max_temp_city = find_extreme_temperatures(data)
    print_summary(avg_temp, avg_humidity, min_temp_city, max_temp_city)


if __name__ == "__main__":
    main()