# Python3 code to demonstrate

# from datetime import datetime
# import pytz

# my_date = "2021-07-05T07:00:00+08:00"
# #expected_result = "Monday 05 July 2021"

# iso_datetime_string = my_date
# # >>> '2019-10-20T15:54:53.840416'

# #DatetImeObj = datetime.datetime.strptime('2018-01-31T09:24:31.488670+00:00', '%Y-%m-%dT%H:%M:%S.%f%z') 
# DatetImeObj = datetime.strptime(my_date, '%Y-%m-%dT%H:%M:%S%z')
# finalDateTime = datetime.strftime(DatetImeObj , "%Y-%m-%d %H:%M") 
# str_day  = datetime.strftime(DatetImeObj , "%A")
# str_date  = datetime.strftime(DatetImeObj , "%d")
# str_month  = datetime.strftime(DatetImeObj , "%B")
# str_year = datetime.strftime(DatetImeObj , "%Y") 

# str_format = datetime.strftime(DatetImeObj , "%A %d %B %Y")

# print(finalDateTime)
# print(f"{str_day} {str_date} {str_month} {str_year}")
# print(str_format)

# temp_in_farenheit = -10
# print(round(((temp_in_farenheit-32)/1.8),1))

# cnt = tot = mean = 0

# weather_data = [49, 57, 56, 55, 53] #[-51, -58, -59, -52, -52, -48, -47, -53]# ["51", "58", "59", "52", "52", "48", "47", "53"]

# for num in weather_data:
#     tot += float(num)
#     cnt += 1
#      #mean = tot/cnt
# print(tot)
# print(cnt)
# print(mean)

# #temperatures = [10.4, 14.5, 12.9, 8.9, 10.5, 11.7] 
# weather_data = ["49", "57", "56", "55", "53", "49"]
# #temperatures = [-10, -8, 2, -16, 4]
# #weather_data = [49, 57, 56, 55, 53, 49] 
# #weather_data = [49, 57, 56, 55, 53]
# val_idx = min_val_idx = 0

# if weather_data:
#     min_val = float(min(weather_data))
#     #for val in weather_data:
#     #min_val_idx = [i 
#     for i in range(len(weather_data)):
#         if float(weather_data[i])==min_val:
#             min_val_idx = float(weather_data[i])
#             val_idx = i
#     print(min_val_idx, val_idx)
        


# self.example_one = [
#             ["2021-07-02T07:00:00+08:00", 49, 67],
#             ["2021-07-03T07:00:00+08:00", 57, 68],
#             ["2021-07-04T07:00:00+08:00", 56, 62],
#             ["2021-07-05T07:00:00+08:00", 55, 61],
#             ["2021-07-06T07:00:00+08:00", 53, 62]
#         ]

# import csv

# csv_file = "tests/data/example_three.csv"
# csv_list = []

# with open(csv_file, encoding="utf-8") as csv_file:
#     next(csv_file)
#     reader = csv.reader(csv_file, delimiter=",")
#     for row in reader:
#         if row:
#             csv_list.append([row[0],int(row[1]),int(row[2])])            
#     #for items in csv_list:
#     print(csv_list)        


"""Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
"""
# 5 Day Overview
#   The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
#   The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
#   The average low this week is 12.2°C.
#   The average high this week is 17.8°C.

list = [
        ["2021-07-02T07:00:00+08:00", 49, 67],
        ["2021-07-03T07:00:00+08:00", 57, 68],
        ["2021-07-04T07:00:00+08:00", 56, 62],
        ["2021-07-05T07:00:00+08:00", 55, 61],
        ["2021-07-06T07:00:00+08:00", 53, 62]
    ]

print(f"{len(list)} Day Overview")

list_temp = []

for row in list:
    print(row[1])
    list_temp.append(row[1])
print(list_temp)

