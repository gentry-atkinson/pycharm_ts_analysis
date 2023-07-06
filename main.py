import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import logging
from datetime import datetime
from decompose_signal import print_naive_analysis

DATA_PATH = 'data/'

if __name__ == '__main__':
    # Reading training data from CSV
    logging.basicConfig(filename='log.txt', level=logging.INFO)
    logging.info("Getting Delhi Temps from file "+datetime.now().strftime("%H:%M:%S"))
    train_df = pd.read_csv(os.path.join(DATA_PATH, 'DailyDelhiClimateTest.csv'))

    # Set up 2x2 plots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

    # Load temps into array and print plot
    temps = np.array(train_df['meantemp'].values.tolist())
    ax1.set_title("Temperature")
    ax1.plot(range(temps.shape[0]), temps)
    logging.info("Temps plotted")

    # Load hums into array and print plot
    hums = np.array(train_df['humidity'].values.tolist())
    ax2.set_title("Humidity")
    ax2.plot(range(hums.shape[0]), hums)
    logging.info("Humidity plotted")

    # Load wind speeds into array and print plot
    w_speeds = np.array(train_df['wind_speed'].values.tolist())
    ax3.set_title("W. Speed")
    ax3.plot(range(w_speeds.shape[0]), w_speeds)
    logging.info("Wind speed plotted")

    # Load air pressure into array and print plot
    press = np.array(train_df['wind_speed'].values.tolist())
    ax4.set_title("Pressure")
    ax4.plot(range(press.shape[0]), press)
    logging.info("Air pressure plotted")

    # Saving plots
    fig.tight_layout()
    plt.savefig("weather_data.png")
    logging.info("Weather plot saved")

    print_naive_analysis(temps, "temperature")
    print_naive_analysis(hums, "humidity")
    print_naive_analysis(w_speeds, "wind_speed")
    print_naive_analysis(press, "pressure")
