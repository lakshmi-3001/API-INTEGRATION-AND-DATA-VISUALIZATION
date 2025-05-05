# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY NAME : CODTECH IT SOLUTIONS PVT.LTD*

NAME : VIJAYALAXMI ACHARYA

INTERN ID : CT04DA24

DOMAIN : PYTHON PROGRAMMING

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH

DESCRIPTION :
API Integration and Data Visualization with JSON and Matplotlib

In this script, I've integrated an API to fetch weather data for a user-specified city and then visualized key aspects of that data using Matplotlib.  My approach leverages the requests library to handle the API call, the json library to process the API response, and Matplotlib for creating informative visualizations.

1.  Fetching Weather Data from OpenWeatherMap API

API Request:  I start by taking the user's city name as input.  Then, I construct the API URL using the city name and my API key for the OpenWeatherMap API.  I make a GET request to this URL using the requests library to retrieve the current weather data.

JSON Response:  The API responds with the weather data in JSON format.  I parse this JSON data into a Python dictionary using response.json().  For debugging and inspection, I've included a formatted print of the raw JSON data using json.dumps(data, indent=4).

2.  Data Visualization with Matplotlib

I used Matplotlib to create two visualizations to provide a clear understanding of the weather conditions:

Bar Chart of Key Weather Metrics:

to extract the temperature, "feels like" temperature, and humidity from the API response.

I created a bar chart using plt.bar() to display these values.  The x-axis represents the weather parameters (temperature, etc.), and the y-axis represents their corresponding values.

I added a title, label the y-axis, and include a grid for better readability.

Pie Chart of Cloud Coverage:

I extract the cloud coverage percentage from the API response. calculate the percentage of "clear" sky by subtracting the cloud coverage from 100.

I created a pie chart using plt.pie() to visualize the proportion of clear and cloudy skies.  The chart displays the percentages of clear and cloudy conditions, providing a quick visual representation of the sky condition.
