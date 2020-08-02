import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

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

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    cel = round((((temp_in_farenheit - 32) * 5) / 9),1)
    return cel


def calculate_mean(total_sum, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = round(total_sum / num_items, 1)
    return mean

def days_in_data(len_dict):
    """Calculates the number of days in the formatted json data file.
    
    Args:
        len_dict: integer representing the number of days in the forecast.
    Returns:
        A list for the number of days in the weather forecast file.
    """
    count_day = 0
    days_list = []
    for i in range(len_dict):
        days_list.append(count_day)
        count_day += 1
    return (days_list)


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    # Load json data file
    
    with open(forecast_file) as json_file:
        json_data = json.load(json_file)
    
    # Set Variables, Dictionaries and Lists
    days_list = []
    temp_dict = {}
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
        
        temp_dict[day] = [min_temp, max_temp, date]
        daily_dict[day] = [date, min_temp, max_temp, day_desc, chance_rain_day, night_desc, chance_rain_night]
    #                       0        1          2         3          4              5              6               
    
    # print(temp_dict)
    # print(daily_dict)

    # Calculate Minimum, Maximum and Mean temperatures

    mean_min = format_temperature(calculate_mean(total_sum_min, num_items))
    # print(mean_min)
    mean_max = format_temperature(calculate_mean(total_sum_max, num_items))
    # print(mean_max)

    # Format Minimum and Maximum temperatures
    min_temp_format = format_temperature(t_temp_min)
    max_temp_format = format_temperature(t_temp_max)

    ##############################################################################################

    # Print messages to user

    str_Output = ""
    Output_gen1 = (f"{num_items} Day Overview\n")
    Output_gen2 = (f"    The lowest temperature will be {min_temp_format}, and will occur on {t_temp_mindate}.\n")
    Output_gen3 = (f"    The highest temperature will be {max_temp_format}, and will occur on {t_temp_maxdate}.\n")
    Output_gen4 = (f"    The average low this week is {mean_min}.\n")
    Output_gen5 = (f"    The average high this week is {mean_max}.\n")
    str_Output = Output_gen1 + Output_gen2 + Output_gen3 + Output_gen4 + Output_gen5
    for key, value in daily_dict.items():
        Output_daily0 = ("\n")
        Output_daily1 = (f"-------- {value[0]} --------\n")
        Output_daily2 = (f"Minimum Temperature: {format_temperature(value[1])}\n")
        Output_daily3 = (f"Maximum Temperature: {format_temperature(value[2])}\n")
        Output_daily4 = (f"Daytime: {value[3]}\n")
        Output_daily5 = (f"    Chance of rain:  {value[4]}%\n")
        Output_daily6 = (f"Nighttime: {value[5]}\n")
        Output_daily7 = (f"    Chance of rain:  {value[6]}%\n")
        str_Output = str_Output + Output_daily0 + Output_daily1 + Output_daily2 + Output_daily3 + Output_daily4 + Output_daily5 + Output_daily6 + Output_daily7
    str_Output = str_Output +"\n"

    return str_Output
    
if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))

# if __name__ == "__main__":
#     process_weather("data/forecast_5days_b.json")

