import json
from datetime import datetime

###################################################################################
# Load json data file

with open("data/forecast_8days.json") as json_file:
    json_data = json.load(json_file)

# print(json_data)

###################################################################################

# Functions

def convert_f_to_c(temp_in_farenheit):
    cel = round((((temp_in_farenheit - 32) * 5) / 9),1)
    return cel

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    temp = str(temp)
    DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"
    return f"{temp}{DEGREE_SYMBOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")

def calculate_mean(total_sum, num_items):
    mean = round(total_sum / num_items, 1)
    return mean
    # print(f"{mean:.1f}")

def days_in_data(len_days):
    count_day = 0

    for i in range(days):
        days_list.append(count_day)
        count_day += 1
    return (days_list)

###################################################################################

# Set Variables, Dictionaries and Lists
days_list = []
# temp_dict = {}
daily_dict = {}

num_items = 0
total_sum_min = 0
total_sum_max = 0
days = len(json_data['DailyForecasts'])
days_list = days_in_data(days)

t_temp_min = 100
t_temp_max = 0
# Pull through the data

for day in days_list:
    num_items += 1
    date = convert_date(json_data['DailyForecasts'][day]['Date'])
    min_temp = convert_f_to_c(json_data['DailyForecasts'][day]['Temperature']['Minimum']['Value'])
    total_sum_min += min_temp
    max_temp = convert_f_to_c(json_data['DailyForecasts'][day]['Temperature']['Maximum']['Value'])
    total_sum_max += max_temp
    day_desc = json_data['DailyForecasts'][day]['Day']['LongPhrase']
    chance_rain_day = json_data['DailyForecasts'][day]['Day']['RainProbability']
    night_desc = json_data['DailyForecasts'][day]['Night']['LongPhrase']
    chance_rain_night = json_data['DailyForecasts'][day]['Night']['RainProbability']
    if min_temp < t_temp_min:
        t_temp_min = min_temp
        t_temp_mindate = date
    else:
        pass
    if max_temp > t_temp_max:
        t_temp_max = max_temp
        t_temp_maxdate = date
    else:
        pass
    # temp_dict = [date, min_temp, max_temp]
    daily_dict[day] = [date, min_temp, max_temp, day_desc, chance_rain_day, night_desc, chance_rain_night]

#                       0        1          2         3         4            5              6               7
print(t_temp_min)
print(t_temp_mindate)
print(t_temp_max)
print(t_temp_maxdate)

# print(temp_dict)
# print(daily_dict)
# Calculate Minimum, Maximum and Mean temperatures

mean_min = format_temperature(calculate_mean(total_sum_min, num_items))
# print(mean_min)
mean_max = format_temperature(calculate_mean(total_sum_max, num_items))
# print(mean_max)

# Format Minimum and Maximum temperatures

# minimum = min(temp_dict.values())
# minimum_date = minimum[2]
# min_temp_format = format_temperature(minimum[0])

# maximum = max(temp_dict.values())
# maximum_date = maximum[2]
# max_temp_format = format_temperature(maximum[1])

##############################################################################################

# Print messages to user

print("5 Day Overview")
print(f"    The lowest temperature will be {min_temp_format}, and will occur on {minimum_date}.")
print(f"    The highest temperature will be {max_temp_format}, and will occur on {maximum[3]}.")
print(f"    The average low this week is {mean_min}.")
print(f"    The average high this week is {mean_max}.")
for key, value in my_dict.items():
    print()
    print(f"-------- {value[1]} --------")
    print(f"Minimum Temperature: {value[0]}")
    print(f"Maximum Temperature: {value[2]}")
    print(f"Daytime: {value[4]}")
    print(f"    Chance of rain:  {value[5]}%")
    print(f"Nighttime: {value[6]}")
    print(f"    Chance of rain:  {value[7]}%")