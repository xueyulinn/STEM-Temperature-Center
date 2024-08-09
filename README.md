# STEM Center Temperature Project

This project is part of the course Object-Oriented Programming in Python. It is designed to manage and analyze temperature data collected from various sensors in a STEM center. The program processes temperature data files, applies filters, and provides summary statistics, averages, and visual representations of the data.

## Features

- **Process Temperature Data**: Load and process temperature data files, storing the data for further analysis.
- **Temperature Summary Statistics**: Calculate and display the minimum, maximum, and average temperatures for selected sensors.
- **Average Temperature by Day and Time**: Print a table showing the average temperature by day of the week and hour of the day.
- **Unit Conversion**: Convert temperature data between Celsius, Fahrenheit, and Kelvin.
- **Sensor Filtering**: Enable or disable specific sensors to focus on relevant data.
- **Histogram Display**: (Placeholder) Display a histogram of temperature data (functionality not yet implemented).

## Components

### 1. `TempDataset` Class
- **Attributes**:
  - `_name`: The name of the dataset.
  - `_data_set`: The dataset containing temperature data.
  - `population`: The number of instances of the class.

- **Methods**:
  - `process_file(filename)`: Loads temperature data from a file.
  - `get_summary_statistics(filter_list)`: Returns the minimum, maximum, and average temperature for active sensors.
  - `get_avg_temperature_day_time(filter_list, day, time)`: Returns the average temperature for a specific day and time.
  - `get_num_temps(filter_list, lower_bound, upper_bound)`: (Placeholder) Returns the number of temperature readings within a specified range.
  - `get_loaded_temps()`: Returns the number of samples loaded into the dataset.

### 2. Recursive Sort Function
- **`recursive_sort(list_to_sort, key)`**: Recursively sorts a list of tuples based on a specified key.

### 3. Unit Conversion Function
- **`convert_units(celsius_value, units)`**: Converts a temperature from Celsius to the specified unit (Celsius, Fahrenheit, or Kelvin).

### 4. User Interface Functions
- **`print_menu()`**: Displays the main menu.
- **`new_file(dataset)`**: Prompts the user to load a new dataset.
- **`choose_units()`**: Allows the user to select the temperature unit (Celsius, Fahrenheit, or Kelvin).
- **`change_filter(sensors, sensor_list, filter_list)`**: Enables or disables sensors for filtering.
- **`print_summary_statistics(dataset, active_sensors)`**: Prints summary statistics (min, max, avg) for active sensors.
- **`print_temp_by_day_time(dataset, active_sensors)`**: Prints a table of average temperatures by day and time.
- **`print_histogram(dataset, active_sensors)`**: (Placeholder) Displays a histogram of temperature data.

### 5. Global Variables
- **`current_unit`**: Tracks the current temperature unit.
- **`UNITS`**: A dictionary mapping unit types to their names and symbols.
- **`DAYS`**: A dictionary mapping day indices to day names.
- **`HOURS`**: A dictionary mapping hour indices to hour ranges.
- **`sensors`**: A dictionary mapping sensor IDs to sensor names and indices.
- **`sensor_list`**: A list of sensors for use in filtering and display.
- **`filter_list`**: A list of active sensors for filtering data.

## Usage

1. **Load a Dataset**: Use the menu option to load a new temperature dataset from a file.
2. **Choose Units**: Select the temperature unit to be used (Celsius, Fahrenheit, Kelvin).
3. **Filter Sensors**: Enable or disable specific sensors to focus on relevant temperature data.
4. **View Summary Statistics**: Display the minimum, maximum, and average temperatures for the selected sensors.
5. **Print Temperature by Day and Time**: View a table showing the average temperatures across different days and hours.
6. **Exit**: Close the program.

## Example
Here is an example of how the program might be used:

```bash
STEM Center Temperature Project
Yulin Xue
Main Menu
---------
1 - Process a new data file
2 - Choose unit
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

None
What is your choice? 4
Please load data file and make sure at least one sensor is active

Main Menu
---------
1 - Process a new data file
2 - Choose unit
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

None
What is your choice? 1
Please enter the filename of the new dataset: Temperatures2022-03-07.csv
Loaded 11724 samples

Please provide a 3 to 20 character name for the dataset Test Week: aaa

Main Menu
---------
1 - Process a new data file
2 - Choose unit
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

20.45544117647059
What is your choice? 4
Summary statistics for Test Week
Minimum Temperature: 16.55 C
Maximum Temperature: 28.42 C
Average Temperature: 21.47 C

Main Menu
---------
1 - Process a new data file
2 - Choose unit
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

20.45544117647059
What is your choice? 2
Current unit is Celsius
Choose new units:
0 - Celsius
1 - Fahrenheit
2 - Kelvin
Which unit?
1

Main Menu
---------
1 - Process a new data file
2 - Choose unit
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

20.45544117647059
What is your choice? 4
Summary statistics for Test Week
Minimum Temperature: 61.79 F
Maximum Temperature: 83.16 F
Average Temperature: 70.64 F

Main Menu
---------
1 - Process a new data file
2 - Choose unit
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

20.45544117647059
What is your choice? 3

4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g. 4201) or x to end 4201

4201: Foundations Lab
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g. 4201) or x to end 4204

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g. 4201) or x to end x

Main Menu
---------
1 - Process a new data file
2 - Choose unit
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

19.910638297872342
What is your choice? 4
Summary statistics for Test Week
Minimum Temperature: 61.79 F
Maximum Temperature: 83.16 F
Average Temperature: 70.13 F

Main Menu
---------
1 - Process a new data file
2 - Choose unit
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

19.910638297872342
What is your choice? 3

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g. 4201) or x to end 4205

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g. 4201) or x to end 4213

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g. 4201) or x to end 4218

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room
Out: Outside [ACTIVE]

Type the sensor number to toggle (e.g. 4201) or x to end Out

4201: Foundations Lab
4204: CS Lab
4205: Tiled Room
4213: STEM Center
4218: Workshop Room
Out: Outside

Type the sensor number to toggle (e.g. 4201) or x to end x

Main Menu
---------
1 - Process a new data file
2 - Choose unit
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

None
What is your choice? 4
Please load data file and make sure at least one sensor is active

Main Menu
---------
1 - Process a new data file
2 - Choose unit
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

None
What is your choice? 7
Thank you for using the STEM Center Temperature Project
>>> 
