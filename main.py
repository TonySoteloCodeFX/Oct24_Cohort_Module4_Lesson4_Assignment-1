from helper import hr

class WeatherData:
    def __init__(self):
        self.data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
    
    def get_weather(self, city):
        """Returns weather data for a given city."""
        return self.data.get(city, None)

class WeatherReport:
    @staticmethod
    def format(data):
        if data is None:
            hr(50)
            return "Weather data not available"

        city = data.get("city", "Unknown city")
        temperature = data.get("temperature", "Unknown temperature")
        condition = data.get("condition", "Unknown condition")
        humidity = data.get("humidity", "Unknown humidity")

        weather_report = (
            f"Weather in {city}: {temperature}°F, {condition}, "
            f"Humidity: {humidity}%"
        )

        return weather_report

class WeatherFetcher:
    """Returns weather data of a given city."""
    def __init__(self, weather_data):
        self.weather_data = weather_data

    def fetch(self, city):
        hr(50)
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get_weather(city)

class WeatherApp:
    def __init__(self):
        self.weather_data = WeatherData()
        self.weather_fetcher = WeatherFetcher(self.weather_data)
        self.weather_report = WeatherReport()

    def get_city_input(self):
        hr(50)
        city = input("Enter the city for the weather forecast or 'exit' to quit: ").strip()
        return city
    
    def get_detailed_input(self):
        hr(50)
        detailed_input = input("Do you want a detailed forecast? (yes/no): ").strip().lower()
        
        if detailed_input == 'yes':
            return True
        elif detailed_input == 'no':
            return False
        else:
            print("Invalid input. Defaulting to 'no'.")
            return False

    def get_forecast(self, city):
        """Returns the weather data for given city."""
        return self.weather_fetcher.fetch(city)

    def display_forecast(self, city: str, detailed: bool):
        """Displays forecast."""
        data = self.get_forecast(city)
        
        if data is None:
            print("Weather data not available.")
            hr(50)
            return
        
        forecast = self.weather_report.format(data)
        print(forecast)

        if detailed:
            temperature = data.get("temperature", "Unknown temperature")
            humidity = data.get("humidity", "Unknown humidity")
            condition = data.get("condition", "Unknown condition")
            
            print(f"Detailed Forecast for {city}:")
            print(f"  - Temperature: {temperature}°F")
            print(f"  - Condition: {condition}")
            print(f"  - Humidity: {humidity}%")
        
        hr(50)

    def run(self):
        while True:
            city = self.get_city_input()
            if city.lower() == 'exit':
                print("Goodbye!")
                break

            detailed = self.get_detailed_input()
            self.display_forecast(city, detailed)

if __name__ == "__main__":
    app = WeatherApp()
    app.run()
