"""
Assignment 11: Pandas Table with Temperature Data
Submitted by Yulin Xue
Submitted:  March 24, 2024

Assignment 11: This assignment implements one function
              print_temp_by_day_time() - print a table that shows
              the average temperature in our labs by day of week
              and hour of day.
"""
import pandas as pd


class TempDataset:
    """ a class used to manage the temperature data

      Attributes
      _name : string
          the name of the dataset
      _date_set : obj
          the dataset containing data
      population : int
          the number of instances

      """
    # constants
    DEFAULT_NAME = "Unnamed"
    DEFAULT_DATA = []
    MIN_STR = 3
    MAX_STR = 20
    # class variable
    population = 0

    def __init__(self):
        self._name = TempDataset.DEFAULT_NAME
        self._data_set = TempDataset.DEFAULT_DATA

        TempDataset.population += 1

    def process_file(self, filename):
        """ open a file and store the data into
            the class variable _data_set"""
        try:
            self._data_set = []
            my_file = open(filename, "r")
            for line in my_file:
                lst = line.split(",")
                if lst[3] == "TEMP":
                    day, time, sensor, temp = (int(lst[0]),
                                               (float(lst[1]) * 24), int(lst[2]), float(lst[4]))
                    self._data_set.append((day, time, sensor, temp))
            return True
        except FileNotFoundError:
            # cannot open the file
            return False

    def get_summary_statistics(self, filter_list):
        """ return a tuple of floats with the minimum, maximum,
            and average temperature of active sensors """

        # return None if no dataset is loaded
        if not self._data_set or len(filter_list) == 0:
            return None

        # store temperature data in a list
        active_sensors_data = [data[3] for data in self._data_set
                               if data[2] in filter_list]

        min_temp = active_sensors_data[0]
        max_temp = active_sensors_data[0]
        sum_temp = 0
        for i in range(len(active_sensors_data)):
            if active_sensors_data[i] < min_temp:
                min_temp = active_sensors_data[i]

            if active_sensors_data[i] > max_temp:
                max_temp = active_sensors_data[i]

            sum_temp += active_sensors_data[i]

        avg_temp = sum_temp / len(active_sensors_data)

        return min_temp, max_temp, avg_temp

    def get_avg_temperature_day_time(self, filter_list, day, time):
        """ return the average temperature of a specific time
            based on active sensors """

        # return None if no dataset loaded and no sensors are active
        if not self._data_set or len(filter_list) == 0:
            return None

        # return None if no readings for active sensors
        active_sensors_data = [data for data in self._data_set
                               if data[2] in filter_list]
        if not active_sensors_data:
            return None

        # store temperature in a list
        filtered_data = [data[3] for data in active_sensors_data
                         if data[0] == day and time <= data[1] <= time + 1]

        # calculate the avg temperature
        sum_temp = 0
        number = len(filtered_data)

        for i in filtered_data:
            sum_temp += i

        avg_temp = sum_temp / number

        return avg_temp

    def get_num_temps(self, filter_list, lower_bound, upper_bound):
        if not self._data_set:
            return None
        return 0

    def get_loaded_temps(self):
        """ return the number of samples that were successfully
            loaded otherwise return None"""
        if not self._data_set:
            return None
        return len(self._data_set)

    @property
    def data_set(self):
        return self._data_set

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) < TempDataset.MIN_STR or len(name) > TempDataset.MAX_STR:
            raise ValueError
        self._name = name

    @classmethod
    def get_num_objects(cls):
        return cls.population


def recursive_sort(list_to_sort, key: 0):
    """accept and sort list using recursion
       list_to_sort is a list of tuples
       key refers to the value in the tuple for sorting
    """
    # escape case
    if len(list_to_sort) == 1:
        return list_to_sort
    # copy the parameter so change the order of items
    # will not affect the passed parameter
    list_copy = list_to_sort[:]
    # this loop is to find the largest item and put it at last
    for i in range(len(list_copy) - 1):
        if list_copy[i][key] > list_copy[i + 1][key]:
            # swap the items using unpacking
            list_copy[i], list_copy[i + 1] = list_copy[i + 1], list_copy[i]
    # call itself to get the ordered list and
    # concatenate with the largest item
    list_sorted = recursive_sort(list_copy[:-1], key) + [(list_copy[-1])]

    return list_sorted


def convert_units(celsius_value, units):
    """accept and convert any Celsius value"""

    if type(celsius_value) not in (int, float):
        return None
    if units == 0:
        return celsius_value
    elif units == 1:
        return celsius_value * 9 / 5 + 32
    elif units == 2:
        return celsius_value + 273.15
    # return error code None
    else:
        return None


def print_menu():
    """provide the interface for the program"""
    menu = """
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
"""
    print(menu)


def new_file(dataset):
    """open a new file"""

    file_name = input("Please enter the filename of the new dataset: ")
    if not dataset.process_file(file_name):
        # unable to load the file
        print("Failed to load the file!")
        # return to the main()
        return

    sample_number = dataset.get_loaded_temps()
    print(f"Loaded {sample_number} samples\n")

    while True:
        dataset_name = input(
            "Please provide a 3 to 20 character name for the dataset: ")
        try:
            dataset.name = dataset_name
            break
        except ValueError:
            print("Provided name is illegal!")


def choose_units():
    """print current units and available units
        and change current units"""
    global current_unit
    global UNITS
    print(f"Current unit in {UNITS[current_unit][0]}")
    while True:
        print("Choose new unit:")
        for k in UNITS:
            print(f"{k} - {UNITS[k][0]}")
        try:
            new_unit = int(input("Which unit?\n"))
            if new_unit not in UNITS.keys():
                print("Please choose a unit from the list")
            else:
                current_unit = new_unit
                break
        except ValueError:
            print("*** Please enter a number only ***")


def change_filter(sensors, sensor_list, filter_list):
    """change the filter"""
    while True:
        # call print_filter
        print()
        print_filter(sensor_list, filter_list)
        # prompt the user for input
        ans = input("\nType the sensor to toggle (e.g. 4201) or x to end ")
        # determine whether the input is legal
        if ans not in sensors.keys() and ans != 'x':
            print("Invalid Sensor")
        elif ans == 'x':
            # exit the loop
            break
        else:
            # add or remove from filter_list
            sensor = sensors.get(ans)[1]
            if sensor in filter_list:
                # remove filter
                filter_list.remove(sensor)
            else:
                # add filter
                filter_list.append(sensor)


def print_summary_statistics(dataset, active_sensors):
    """print min, max and avg temp data of active sensors"""

    data_summary = dataset.get_summary_statistics(active_sensors)
    dataset_name = dataset.name

    if data_summary is None:
        print("Please load data file and make sure at least one sensor is active")
    else:
        temp_unit = UNITS[current_unit][1]
        # rounded to 2 decimals
        min_temp = round(convert_units(data_summary[0], current_unit), 2)
        max_temp = round(convert_units(data_summary[1], current_unit), 2)
        avg_temp = round(convert_units(data_summary[2], current_unit), 2)

        print(f"Summary statistics for {dataset_name}\n"
              f"Minimum Temperature: {min_temp} {temp_unit}\n"
              f"Maximum Temperature: {max_temp} {temp_unit}\n"
              f"Average Temperature: {avg_temp} {temp_unit}")


def print_temp_by_day_time(dataset, active_sensors):
    """print the average temperature in
       our labs by day of week and hour
       of day based on active sensors"""
    if dataset.get_loaded_temps() is None:
        print("No File Loaded")
    else:
        temp_unit = UNITS[current_unit][0]
        print(f"Average Temperatures for {dataset.name}")
        print(f"Units are in {temp_unit}")

        # initialize a dic
        daily_avg_temp = {}
        
        for day in DAYS:
            # collect temp with a list while convert to current unit
            temp_lst = [
                convert_units(dataset.get_avg_temperature_day_time
                              (active_sensors, day, hour), current_unit)
                for hour in HOURS]

            # populate data
            daily_avg_temp[DAYS[day]] = temp_lst

        columns = [day for day in DAYS.values()]
        indexes = [hour for hour in HOURS.values()]

        my_data_frame = pd.DataFrame(
            data=daily_avg_temp, index=indexes, columns=columns)

        # round 1 decimal element-wise
        my_data_frame = my_data_frame.round(1)

        # fill none with '---'
        my_data_frame = my_data_frame.fillna("---")

        print(my_data_frame)


def print_histogram(dataset, active_sensors):
    """print histogram"""
    print("Print Histogram Function Called")


def print_header():
    """print project and student name"""

    print("STEM Center Temperature Project\nYulin Xue")


def print_filter(sensor_list, filter_list):
    """print the list of filters and display which
    ones are currently active"""
    # traverse sensor_list and determine which sensor is active
    for i in sensor_list:
        if i[2] in filter_list:
            print(f"{i[0]}: {i[1]} [ACTIVE]")
        else:
            print(f"{i[0]}: {i[1]} ")


def main():
    """ unit test code """


# global variable
current_unit = 0

# global constant
UNITS = {
    0: ("Celsius", "C"),
    1: ("Fahrenheit", "F"),
    2: ("Kelvin", "K"),
}

current_set = TempDataset()

DAYS = {
    0: "SUN",
    1: "MON",
    2: "TUE",
    3: "WED",
    4: "THU",
    5: "FRI",
    6: "SAT"
}

HOURS = {
    0: "Mid-1AM  ",
    1: "1AM-2AM  ",
    2: "2AM-3AM  ",
    3: "3AM-4AM  ",
    4: "4AM-5AM  ",
    5: "5AM-6AM  ",
    6: "6AM-7AM  ",
    7: "7AM-8AM  ",
    8: "8AM-9AM  ",
    9: "9AM-10AM ",
    10: "10AM-11AM",
    11: "11AM-NOON",
    12: "NOON-1PM ",
    13: "1PM-2PM  ",
    14: "2PM-3PM  ",
    15: "3PM-4PM  ",
    16: "4PM-5PM  ",
    17: "5PM-6PM  ",
    18: "6PM-7PM  ",
    19: "7PM-8PM  ",
    20: "8PM-9PM  ",
    21: "9PM-10PM ",
    22: "10PM-11PM",
    23: "11PM-MID ",
}

sensors = {'4213': ('STEM Center', 0), '4201': ('Foundations Lab', 1),
           '4204': ('CS Lab', 2), '4218': ('Workshop Room', 3),
           '4205': ('Tiled Room', 4), 'Out': ('Outside', 5)}

# create sensor_list using list comprehension
sensor_list = [(key, sensors[key][0], sensors[key][1]) for key in sensors]
# create filter_list using list comprehension.
filter_list = [sensors[key][1] for key in sensors]

# unit Test Code follows
# sort sensor_list before while loop
sorted_list = recursive_sort(sensor_list, 0)

print_header()
while True:
    # show the interface
    print_menu()

    try:
        # put a space after the prompt to increase readability
        user_option = int(input("What is your choice? "))
        # call the function according to user's choice
        if user_option == 1:
            new_file(current_set)
        elif user_option == 2:
            choose_units()
        elif user_option == 3:
            change_filter(sensors, sorted_list, filter_list)
        elif user_option == 4:
            print_summary_statistics(current_set, filter_list)
        elif user_option == 5:
            print_temp_by_day_time(current_set, filter_list)
        elif user_option == 6:
            print_histogram(current_set, filter_list)
        # exit the interface
        elif user_option == 7:
            print("Thank you for using the STEM Center Temperature Project")
            break
        else:
            print("Invalid Choice, please enter an integer between 1 and 7.")
    # catch the error
    except ValueError:
        print("*** Please enter a number only ***")

if __name__ == "__main__":
    main()
