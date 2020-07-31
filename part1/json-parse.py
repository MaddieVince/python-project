import json

with open("data/forecast_5days_a.json") as json_file:
    json_data = json.load(json_file)

# print(json_data)

daily_temp_min = []

days = [0,1,2,3,4]
min_temp_dict = {}
max_temp_dict = {}

for day in days:
    temp = json_data['DailyForecasts'][day]['Temperature']['Minimum']['Value']
    date_min = json_data['DailyForecasts'][day]['Date']
    min_temp_dict[day] = [temp, date_min]

minimum = min(min_temp_dict.values())

print(f"Minimum temperature of {minimum[0]} will happen on {minimum[1]}")

# print(min_temp_dict)
        
for day in days:
    temp = json_data['DailyForecasts'][day]['Temperature']['Maximum']['Value']
    date_max = json_data['DailyForecasts'][day]['Date']
    max_temp_dict[day] = [temp, date_min]

maximum = max(max_temp_dict.values())

print(f"Maximum temperature of {maximum[0]} will happen on {maximum[1]}")

# print(maximum)
# print(max_temp_dict)

# print(min_temp_dict[0])

