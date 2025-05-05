# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY NAME : CODTECH IT SOLUTIONS PVT.LTD

NAME : VIJAYALAXMI ACHARYA

INTERN ID : CT04DA24

DOMAIN : PYTHON PROGRAMMING

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH

DESCRIPTION :

**API Integration and Data Visualization with JSON and Matplotlib**

I've integrated an API to fetch weather data for a user-specified city and then visualized key aspects of that data using Matplotlib.  My approach leverages the requests library to handle the API call, the json library to process the API response, and Matplotlib for creating informative visualizations.

**1. Fetching Weather Data from OpenWeatherMap API**

API Request:  I start by taking the user's city name as input.  Then, I construct the API URL using the city name and my API key for the OpenWeatherMap API.  I made a GET request to this URL using the requests library to retrieve the current weather data.
JSON Response:  The API responds with the weather data in JSON format.  I parse this JSON data into a Python dictionary using response.json().  For debugging and inspection, I've included a formatted print of the raw JSON data using json.dumps(data, indent=4).

**2. Data Visualization with Matplotlib**

I used Matplotlib to create two visualizations to provide a clear understanding of the weather conditions:

Bar Chart of Key Weather Metrics:

to extract the temperature, "feels like" temperature, and humidity from the API response.
I created a bar chart using plt.bar() to display these values.  The x-axis represents the weather parameters (temperature, etc.), and the y-axis represents their corresponding values.
I added a title, label the y-axis, and include a grid for better readability.

Pie Chart of Cloud Coverage:

To extract the cloud coverage percentage from the API response. calculate the percentage of "clear" sky by subtracting the cloud coverage from 100.
I created a pie chart using plt.pie() to visualize the proportion of clear and cloudy skies.  The chart displays the percentages of clear and cloudy conditions, providing a quick visual representation of the sky condition.

**application of API and data visualization**
1. API (Application Programming Interface) integration allows different software systems to communicate with each other. Its applications include:
**Real-Time Data Access**
Fetching live data (e.g., weather, stock prices, news, cryptocurrency rates) from external services for analysis or display.
**Automation of Workflows**
Automating repetitive tasks by connecting services like Google Sheets, Slack, Gmail, or databases through APIs.
**Machine Learning Model Deployment**
Hosting and using ML models as APIs so other applications (web, mobile, desktop) can send data and receive predictions.
**Payment Gateways**
Integrating APIs like Stripe, PayPal, or Razorpay into apps or websites for secure and smooth transactions.
**Social Media Integration**
Pulling data from platforms like Twitter, Instagram, or YouTube for sentiment analysis, engagement tracking, or marketing analytics.

2.Data visualization is the graphical representation of information and data. Its applications include:
**Exploratory Data Analysis (EDA)**
Understanding patterns, trends, and outliers in a dataset using charts and plots before building models.
**Business Intelligence (BI)**
Dashboards showing KPIs, sales, profits, customer churn, etc., help stakeholders make data-driven decisions (e.g., with Tableau, Power BI).
**Scientific and Medical Research**
Visualizing genome sequences, molecular structures, patient data, or clinical trial results.
**Monitoring Systems**
Visual dashboards to monitor server health, network traffic, or application performance in real time.
**Storytelling with Data**
Making insights understandable and compelling for non-technical audiences using charts, infographics, and interactive reports.

**Output**

![Image](https://github.com/user-attachments/assets/f2f1504d-9651-4ff4-8af1-19fdcd23ea68)

![Image](https://github.com/user-attachments/assets/6e745e60-22ab-4629-baf2-e8ae73c10de7)
