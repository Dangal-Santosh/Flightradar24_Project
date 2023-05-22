from FlightRadar24.api import FlightRadar24API
import re
import csv
import matplotlib.pyplot as plt
import pandas as pd
from itertools import count
from matplotlib.animation import FuncAnimation

fr_api = FlightRadar24API()
flights = fr_api.get_flights()

data = []
for flight in flights:
    data.append(str(flight))

l = []
a = []
c = []
for d in data:
    main_data = d.strip("<>").strip()
    split_data = main_data.split(" - ")
    l.append(split_data[0])
    a.append(split_data[1])
    for g in a:
        c.append(g[9:])

csv_file = 'flight_data.csv'

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Flight', 'Altitude'])

    for i in range(len(l)):
        writer.writerow([l[i], c[i]])

# For visualization
plt.style.use('seaborn-darkgrid')

df = pd.read_csv('flight_data.csv')

fig, ax = plt.subplots(figsize=(10, 2))

def animate(i):
    plt.cla()

    start_index = i * 20
    end_index = (i + 1) * 20

    x_vals = df['Flight'].iloc[start_index:end_index]
    y_vals = df['Altitude'].iloc[start_index:end_index]

    ax.plot(x_vals, y_vals, marker='o', linestyle='-', color='b')

    # Customize plot appearance
    ax.set_xlabel('Flight', fontsize=10)
    ax.set_ylabel('Altitude (ft)', fontsize=12)
    ax.set_title('Flight Altitude Visualization', fontsize=14)
    ax.tick_params(axis='x', rotation=45, labelsize=10)
    ax.set_ylim(bottom=0)  # Set minimum y-axis value to 0
    ax.grid(True, linestyle='--', alpha=0.7)

ani = FuncAnimation(fig, animate, frames=len(df) // 20, interval=8000)
plt.tight_layout()
plt.show()
