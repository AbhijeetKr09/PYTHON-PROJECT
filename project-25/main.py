import csv
import pandas

# with open('./weather_data.csv', mode='r') as weather_data:
#     data = weather_data.readlines()
#     print(data)

# with open('./weather_data.csv', mode='r') as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(row[1])
#     print(temperature)

data = pandas.read_csv('weather_data.csv')

print(data)