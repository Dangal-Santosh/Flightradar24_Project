import csv
import random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generate random flight data
def generate_flight_data():
    flight_name = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=6))
    departure_airport = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
    arrival_airport = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
    airline = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
    return [flight_name, departure_airport, arrival_airport, airline]

# Define the CSV file path
csv_file = 'flight_data_flightradar24.csv'

# Generate flight data for 1000 flights
data = []
for _ in range(1000):
    data.append(generate_flight_data())

# Write data to CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Flight Name', 'Departure Airport', 'Arrival Airport', 'Airline'])  # Write header
    writer.writerows(data)  # Write data rows

print(f"Random flight data has been saved to {csv_file}.")

# Set up the figure and axis
fig, ax = plt.subplots()

# Initialize the empty plot
flight_names = []
departure_airports = []
arrival_airports = []
airlines = []
flight_plot = ax.bar([], [], align='edge', color='deepskyblue', edgecolor='black', linewidth=0.5)

# Set the axis labels and title
ax.set_xlabel('Flight Name', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.set_title('Real-time Flight Data Visualization', fontsize=14, fontweight='bold')

# Set the plot style
plt.style.use('seaborn-whitegrid')

# Function to update the plot
def update_plot(frame):
    # Clear the previous plot
    ax.clear()

    # Read the updated flight data from CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        flight_data = list(reader)

    # Extract flight data columns
    flight_names = [row[0] for row in flight_data[frame:frame+20]]
    departure_airports = [row[1] for row in flight_data[frame:frame+20]]
    arrival_airports = [row[2] for row in flight_data[frame:frame+20]]
    airlines = [row[3] for row in flight_data[frame:frame+20]]

    # Update the plot with new data
    flight_plot = ax.bar(flight_names, range(len(flight_names)), align='edge',
                         color='deepskyblue', edgecolor='black', linewidth=0.5)

    # Set the axis labels and title
    ax.set_xlabel('Flight Name', fontsize=12, fontweight='bold')
    ax.set_ylabel('Count', fontsize=12, fontweight='bold')
    ax.set_title('Real-time Flight Data Visualization', fontsize=14, fontweight='bold')

    # Rotate the x-axis labels for better visibility
    plt.xticks(rotation=45, ha='right', fontsize=8)

    # Set the plot background color
    ax.set_facecolor('#f0f0f0')

# Calculate the total number of frames
total_frames = len(data) - 20

# Animate the plot
ani = animation.FuncAnimation(fig, update_plot, frames=total_frames, interval=4000, repeat=False)

# Display the plot
plt.show()
