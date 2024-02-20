# Wether_Report_Project
This project appears to be a simple weather application implemented in Python. Here's a breakdown of its components and technologies used:

**Python**: The core programming language used for development. Python is a popular choice for its simplicity and versatility.

**Requests Library**: The requests library is used to make HTTP requests to the OpenWeatherMap API to fetch weather data. This library simplifies the process of sending HTTP requests and handling responses.

**OpenWeatherMap API**: This project utilizes the OpenWeatherMap API to obtain weather data. The API provides current weather, forecasts, and other weather-related data based on geographical location.

**Environment Variables**: The project uses environment variables to store sensitive information such as the API key (user_api). This is a common practice for keeping sensitive information secure and separate from the codebase.

**Datetime Module**: The datetime module is used to work with dates and times. In this project, it's used to get the current date and time, which is then formatted and displayed along with the weather data.

**Input Handling**: The project prompts the user to input a city name for which they want to fetch the weather data. This input is then used to construct the API request URL.

**Data Parsing and Display**: After retrieving data from the API, the JSON response is parsed to extract relevant weather information such as temperature, weather description, humidity, and wind speed. This information is then formatted and displayed to the user in a readable format.

Overall, this project demonstrates how to interact with a web API, handle API responses, work with environment variables, and format/display data in a Python console application. It provides a basic example of integrating external APIs into a Python project to retrieve useful information.
