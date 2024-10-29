<h1>Assignments: Clean Code</h1>

<h3>1. Refactoring a Weather Forecast Application into Classes and Modules</h3>

<b>Objective:</b> The aim of this assignment is to refactor an existing Python script for a weather forecast application into a more structured, object-oriented, and modular format. The focus will be on identifying parts of the script that can be encapsulated into classes and organizing these classes into appropriate modules to enhance code readability, maintainability, and scalability.

<b>Task 1:</b> Identifying and Creating Classes Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. Create classes that represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.

<b>Problem Statement:</b> The existing script for the weather forecast application is written in a procedural style and lacks organization.

<b>Code Example:</b> Before Refactoring:

```
# Weather Forecast Application Script

def fetch_weather_data(city):
    # Simulated function to fetch weather data for a given city
    print(f"Fetching weather data for {city}...")
    # Simulated data based on city
    weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }
    return weather_data.get(city, {})

def parse_weather_data(data):
    # Function to parse weather data
    if not data:
        return "Weather data not available"
    city = data["city"]
    temperature = data["temperature"]
    condition = data["condition"]
    humidity = data["humidity"]
    return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

def get_detailed_forecast(city):
    # Function to provide a detailed weather forecast for a city
    data = fetch_weather_data(city)
    return parse_weather_data(data)

def display_weather(city):
    # Function to display the basic weather forecast for a city
    data = fetch_weather_data(city)
    if not data:
        print(f"Weather data not available for {city}")
    else:
        weather_report = parse_weather_data(data)
        print(weather_report)

def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = get_detailed_forecast(city)
        else:
            forecast = display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()
```

<b>Expected Outcome:</b>

Clear definitions of classes such as `WeatherDataFetcher`, `DataParser`, and `UserInterface`, each handling specific parts of the application.

<b>NOTE:</b> Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs. If there are classes/objects, make sure they are instantiated and the methods are called.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.