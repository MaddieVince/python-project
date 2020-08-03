import json
from datetime import datetime
import plotly.express as px
# import plotly.graph_objects as go

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    cel = round((((temp_in_farenheit - 32) * 5) / 9),1)
    return cel

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")

with open("data/forecast_5days_a.json") as json_file:
        json_data = json.load(json_file)

df = json_data

count_day = 0
days = len(json_data['DailyForecasts'])

days_list = []

min_list = []
max_list = []
date_list = []

# Build dataframe for plotly

df = {}

for i in range(days):
    days_list.append(count_day)
    count_day += 1

# Generate Lists for Graph 1 

for day in days_list:
    date = convert_date(json_data['DailyForecasts'][day]['Date'])
    min_temp = convert_f_to_c(json_data['DailyForecasts'][day]['Temperature']['Minimum']['Value'])
    max_temp = convert_f_to_c(json_data['DailyForecasts'][day]['Temperature']['Maximum']['Value'])
    min_list.append(min_temp)
    max_list.append(max_temp)
    date_list.append(date)

# print(max_list)
# print(min_list)
# print(date_list)

df['date'] = date_list
df['Minimum Temperature'] = min_list
df['Maximum Temperature'] = max_list

# print(df)

# Data Input for Graph 1

fig = px.line(
    df,
    y=["Minimum Temperature","Maximum Temperature"],
    x="date",
    title = f"{days} Day Forecast: Minimum and Maximum Temperatures",
    template="plotly_white",
    color_discrete_sequence=["DarkOrchid","CornflowerBlue"] 
)

# Layout changes for Graph 1

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Temperature",
    legend_title="Legend",
    title={
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(
    family="Calibri",
)
)

# Add Hover Effects to Graph 1

fig.update_traces(mode="markers+lines", hovertemplate=None)
fig.update_layout(hovermode="x unified")

fig.show()

# Generate Lists for Graph 2 

# Reset Lists and Dictionaries
df = {}
min_list = []
min_feel_list = []
min_shade_list = []
date_list = []

for day in days_list:
    date = convert_date(json_data['DailyForecasts'][day]['Date'])
    min_temp = convert_f_to_c(json_data['DailyForecasts'][day]['Temperature']['Minimum']['Value'])
    min_feel_temp = convert_f_to_c(json_data['DailyForecasts'][day]['RealFeelTemperature']['Minimum']['Value'])
    min_shade_temp = convert_f_to_c(json_data['DailyForecasts'][day]['RealFeelTemperatureShade']['Minimum']['Value'])
    min_list.append(min_temp)
    min_feel_list.append(min_feel_temp)
    min_shade_list.append(min_shade_temp)
    date_list.append(date)

df['date'] = date_list
df['Minimum Temperature'] = min_list
df['Minimum Feel Temperature'] = min_feel_list
df['Minimum Feel Temperature Shade'] = min_shade_list

# Data Input for Graph 2

fig = px.line(
    df,
    y=["Minimum Temperature","Minimum Feel Temperature","Minimum Feel Temperature Shade"],
    x="date",
    title = f"{days} Day Forecast: Minimum Temperature",
    template="plotly_white",
    color_discrete_sequence=["DarkOrchid","CornflowerBlue", "DarkTurquoise"] 
)

# Layout changes for Graph 2

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Temperature",
    legend_title="Legend",
    title={
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(
    family="Calibri",  
)
)

# Add Hover Effects to Graph 2

fig.update_traces(mode="markers+lines", hovertemplate=None)
fig.update_layout(hovermode="x unified")

fig.show()