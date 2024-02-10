def print_summary(avg_temp, avg_humidity, min_temp_city, max_temp_city):
    print(f"Average Temperature: {avg_temp}")
    print(f"Average Humidity: {avg_humidity}")
    print(f"City with Lowest Temperature: {min_temp_city['city']}, Temp: {min_temp_city['temperature']} & {min_temp_city['condition']} condition")
    print(f"City with Highest Temperature: {max_temp_city['city']}, Temp: {max_temp_city['temperature']} & {max_temp_city['condition']} condition")