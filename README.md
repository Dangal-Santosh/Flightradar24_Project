# Flightradar24_Project
**Title: Flight Altitude Visualization**

**Description:**
The Flight Altitude Visualization script utilizes the FlightRadar24 API to retrieve flight data, specifically flight names and altitudes. The script then processes the data and saves it in a CSV file for further analysis. Additionally, the script leverages the Matplotlib library to create an animated plot that visualizes the flight altitudes over time.
The FlightRadar24 API is accessed to retrieve the latest flight data. The script collects flight information, including flight names and altitudes, and stores it in a list. The data is then processed and separated into two lists, "Flight" and "Altitude." These lists are used to create a CSV file, which contains the flight and altitude data in a structured format.
To provide a visual representation of the flight altitudes, the script utilizes Matplotlib's animation capabilities. The Flight Altitude Visualization plot is animated to display 20 flights at a time, enhancing the clarity of the visualization. Each animation frame updates the plot with the next set of flight data points, creating a dynamic display of the flight altitudes over time.
The plot's appearance is refined by using the "seaborn-darkgrid" style, which provides a visually pleasing and easy-to-read layout. The x-axis labels are rotated by 45 degrees to avoid overlapping text, and the y-axis is set to start from 0 to ensure a proper reference point for altitude values.
The Flight Altitude Visualization script serves as a valuable tool for analyzing flight data and gaining insights into altitude patterns. It can be utilized in various applications, such as aviation research, air traffic analysis, and flight performance evaluations. By visualizing the flight altitudes over time, it enables users to identify trends, patterns, and anomalies in the altitude data, aiding in decision-making and comprehensive data exploration.

**Required Libraries**
To run the Flight Altitude Visualization code, you will need the following libraries:

FlightRadar24: This library provides the FlightRadar24API class for accessing flight data from the FlightRadar24 API. You can install it using the command: pip install FlightRadar24.

re: This library provides support for regular expressions. It is used in the code to manipulate and extract data from flight information. It is a built-in library in Python, so no installation is required.

csv: This library provides functionality for reading and writing CSV files. It is used in the code to create a CSV file and store flight data in it. It is a built-in library in Python, so no installation is required.

matplotlib: This library is used for creating visualizations and plots. It is used in the code to plot the flight altitude data. You can install it using the command: pip install matplotlib.

pandas: This library provides data manipulation and analysis tools. It is used in the code to read and process data from the CSV file. You can install it using the command: pip install pandas.

itertools: This library provides various functions for creating iterators. It is used in the code to generate a count for the animation frames. It is a built-in library in Python, so no installation is required.

matplotlib.animation: This library provides classes for creating animations. It is used in the code to animate the flight altitude plot. It is part of the matplotlib library, so it will be installed when you install matplotlib.

Make sure you have these libraries installed before running the code. You can install any missing libraries using the pip install command followed by the library name.


![image](https://github.com/Dangal-Santosh/Flightradar24_Project/assets/71684338/63d1dd84-1655-4d63-88ec-db587738ae42)
