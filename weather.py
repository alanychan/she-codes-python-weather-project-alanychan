import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


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


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    return round(((float(temp_in_farenheit)-32))/1.8,1)
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


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    csv_list = []

    with open(csv_file, encoding="utf-8") as csv_file:
        next(csv_file)
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            if row:
                csv_list.append([row[0],int(row[1]),int(row[2])]) 
    return(csv_list)
    #pass


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


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
    list_temp = []
    list_temp_high = []
    
    for row in weather_data:
        list_temp.append(row[1])
        list_temp_high.append(row[2])

    return f"{len(weather_data)} Day Overview\n  The lowest temperature will be {(format_temperature(convert_f_to_c((find_min(list_temp)[0]))))}, and will occur on {(convert_date(weather_data[find_min(list_temp)[1]][0]))}.\n  The highest temperature will be {(format_temperature(convert_f_to_c((find_max(list_temp_high)[0]))))}, and will occur on {(convert_date(weather_data[find_max(list_temp_high)[1]][0]))}.\n  The average low this week is {(format_temperature(convert_f_to_c(calculate_mean(list_temp))))}.\n  The average high this week is {(format_temperature(convert_f_to_c(calculate_mean(list_temp_high))))}.\n"
    #pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """  
    str_results = ""

    for row in weather_data:
        str_results = str_results + "---- " + convert_date(row[0]) + " ----\n  Minimum Temperature: " + format_temperature(convert_f_to_c(row[1])) + "\n  Maximum Temperature: " + format_temperature(convert_f_to_c(row[2])) + "\n\n"

    return(str_results)
    #pass
    
   