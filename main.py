from pathlib import Path
from utils import print_summary
from data_handler import read_json_file
from weather_analysis import calculate_averages, find_extreme_temperatures

DATA_FILE = Path("weather_data.json")

def main():
    data = read_json_file(DATA_FILE)
    avg_temp, avg_humidity = calculate_averages(data)
    min_temp_city, max_temp_city = find_extreme_temperatures(data)
    print_summary(avg_temp, avg_humidity, min_temp_city, max_temp_city)

if __name__ == "__main__":
    main()