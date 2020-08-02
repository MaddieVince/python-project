import json
from datetime import datetime

###################################################################################
# Load json data file

with open("data/forecast_5days_a.json") as json_file:
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
my_dict = {}

num_items = 0
total_sum_min = 0
total_sum_max = 0
days = len(json_data['DailyForecasts'])
days_list = days_in_data(days)

# Pull through the data

for day in days_list:
    num_items+= 1
    min_temp = convert_f_to_c(json_data['DailyForecasts'][day]['Temperature']['Minimum']['Value'])
    date_min = json_data['DailyForecasts'][day]['Date']
    total_sum_min += min_temp
    date_min = convert_date(date_min)
    max_temp = convert_f_to_c(json_data['DailyForecasts'][day]['Temperature']['Maximum']['Value'])
    date_max = json_data['DailyForecasts'][day]['Date']
    date_max = convert_date(date_max)
    total_sum_max += max_temp
    day_desc = json_data['DailyForecasts'][day]['Day']['LongPhrase']
    chance_rain_day = json_data['DailyForecasts'][day]['Day']['RainProbability']
    night_desc = json_data['DailyForecasts'][day]['Night']['LongPhrase']
    chance_rain_night = json_data['DailyForecasts'][day]['Night']['RainProbability']
    my_dict[day] = [min_temp, date_min, max_temp, date_max, day_desc, chance_rain_day, night_desc, chance_rain_night]
#                       0        1          2         3         4            5              6               7

# Calculate Minimum, Maximum and Mean temperatures

mean_min = format_temperature(calculate_mean(total_sum_min, num_items))
# print(mean_min)
mean_max = format_temperature(calculate_mean(total_sum_max, num_items))
# print(mean_max)

# Format Minimum and Maximum temperatures

minimum = min(my_dict.values())
minimum_date = minimum[1]
min_temp_format = format_temperature(minimum[0])
maximum = max(my_dict.values())
max_temp_format = format_temperature(maximum[2])

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