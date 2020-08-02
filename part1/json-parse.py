import json

###################################################################################
# Load json data file
###################################################################################

with open("data/forecast_5days_a.json") as json_file:
    json_data = json.load(json_file)

# print(json_data)

###################################################################################
# Functions
###################################################################################

def convert_f_to_c(temp_in_farenheit):
    celsius = round((((temp_in_farenheit - 32) * 5) / 9),1)
    # print(celsius)
    return celsius

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    temp = str(temp)
    DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"
    return f"{temp}{DEGREE_SYBMOL}"

###################################################################################
# Pull through the data
###################################################################################

# Minimum Temperature and Date

daily_temp_min = []

days = [0,1,2,3,4]
min_temp_dict = {}

for day in days:
    min_temp = convert_f_to_c(json_data['DailyForecasts'][day]['Temperature']['Minimum']['Value'])
    min_temp = format_temperature(min_temp)
    date_min = json_data['DailyForecasts'][day]['Date']
    max_temp = convert_f_to_c(json_data['DailyForecasts'][day]['Temperature']['Maximum']['Value'])
    date_max = json_data['DailyForecasts'][day]['Date']
    day_desc = json_data['DailyForecasts'][day]['Day']['LongPhrase']
    chance_rain_day = json_data['DailyForecasts'][day]['Day']['RainProbability']
    night_desc = json_data['DailyForecasts'][day]['Night']['LongPhrase']
    chance_rain_night = json_data['DailyForecasts'][day]['Night']['RainProbability']
    min_temp_dict[day] = [min_temp, date_min, max_temp, date_max, day_desc, chance_rain_day, night_desc, chance_rain_night]
    
print(min_temp_dict)

minimum = min(min_temp_dict.values())
minimum_temp_f = minimum[0]
minimum_temp_c = convert_f_to_c(minimum_temp_f)
minimum_temp_format = format_temperature(minimum_temp_c)

print(minimum_temp_format)



print(f"Minimum temperature of {minimum[0]} will happen on {minimum[1]}")

# Maximum Temperature and Date

# for day in days:
#     temp = json_data['DailyForecasts'][day]['Temperature']['Maximum']['Value']
#     date_max = json_data['DailyForecasts'][day]['Date']
#     max_temp_dict[day] = [temp, date_min]

# maximum = max(max_temp_dict.values())

# print(f"Maximum temperature of {maximum[0]} will happen on {maximum[1]}")

# print(maximum)
# print(max_temp_dict)

# print(min_temp_dict[0])

