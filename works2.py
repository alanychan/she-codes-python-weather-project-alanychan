import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    val_idx = min_val_idx = 0
    if weather_data:
        min_val = float(min(weather_data))

        for i in range(len(weather_data)):
            if float(weather_data[i])==min_val:
                min_val_idx = float(weather_data[i])
                val_idx = i
        return(float(min_val_idx), val_idx)
    else:
        return()
    #pass

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    return round(((float(temp_in_farenheit)-32))/1.8,1)
    #pass

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    DatetImeObj = datetime.strptime(iso_string, '%Y-%m-%dT%H:%M:%S%z')
    return(datetime.strftime(DatetImeObj , "%A %d %B %Y")) 
    #pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    val_idx = max_val_idx = 0
    if weather_data:
        max_val = float(max(weather_data))

        for i in range(len(weather_data)):
            if float(weather_data[i])==max_val:
                max_val_idx = float(weather_data[i])
                val_idx = i
        return(float(max_val_idx), val_idx)
    else:
        return()
    #pass

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    cnt_idx = tot = mean = 0

    for num in weather_data:
        tot += float(num)
        cnt_idx += 1
        mean = tot/cnt_idx
    
    return(mean)
    #pass


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

# weather_data =[
#             ["2020-06-19T07:00:00+08:00", -47, -46],
#             ["2020-06-20T07:00:00+08:00", -51, 67],
#             ["2020-06-21T07:00:00+08:00", 58, 72],
#             ["2020-06-22T07:00:00+08:00", 59, 71],
#             ["2020-06-23T07:00:00+08:00", -52, 71],
#             ["2020-06-24T07:00:00+08:00", 52, 67],
#             ["2020-06-25T07:00:00+08:00", -48, 66],
#             ["2020-06-26T07:00:00+08:00", 53, 66]
#         ]

# list_temp = []
# list_temp_high = []
# # list_idx = 0

# for row in weather_data:
#     list_temp.append(row[1])
#     list_temp_high.append(row[2])

# # print(len(weather_data))
# # print(list_temp_high)
# # print(find_max(list_temp_high))
# # print(convert_f_to_c(find_max(list_temp_high)[0]))
# # print(format_temperature(convert_f_to_c((find_min(list_temp)[0]))))
# # print(convert_date(weather_data[find_min(list_temp)[1]][0]))

# print(f"{len(weather_data)} Day Overview\n  The lowest temperature will be {(format_temperature(convert_f_to_c((find_min(list_temp)[0]))))}, and will occur on {(convert_date(weather_data[find_min(list_temp)[1]][0]))}.\n  The highest temperature will be {(format_temperature(convert_f_to_c((find_max(list_temp_high)[0]))))}, and will occur on {(convert_date(weather_data[find_max(list_temp_high)[1]][0]))}.\n  The average low this week is {(format_temperature(convert_f_to_c(calculate_mean(list_temp))))}.\n  The average high this week is {(format_temperature(convert_f_to_c(calculate_mean(list_temp_high))))}.\n")

weather_data = [
            ["2021-07-02T07:00:00+08:00", 49, 67],
            ["2021-07-03T07:00:00+08:00", 57, 68],
            ["2021-07-04T07:00:00+08:00", 56, 62],
            ["2021-07-05T07:00:00+08:00", 55, 61],
            ["2021-07-06T07:00:00+08:00", 53, 62]
        ]

weather_data.append("\n")

str_break = ""
txt_min = "Minimum"
txt_max = "Maximum"
x = txt_min.rjust(9, " ")
y = txt_max.rjust(9, " ")
counter = 0
tot = len(weather_data)

for row in weather_data:
    counter += 1
    if tot == counter:
        print(weather_data[-1])
    else:
        print(f"---- {convert_date(row[0])} ----\n{x} Temperature: {format_temperature(convert_f_to_c(row[1]))}\n{y} Temperature: {format_temperature(convert_f_to_c(row[2]))}\n")

# with open("tests\expected_output\example_one_daily_summary.txt", "r") as f:
#     print(f.readlines())