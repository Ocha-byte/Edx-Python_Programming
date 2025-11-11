import asyncio
import time
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
import smbus2

# Initialize I2C bus
I2C_ADDRESS = 0x48  # Address of the SGM5304 sensor
I2C_BUS = smbus2.SMBus(1)  # Use I2C bus 1


# Read temperature from SGM5304 sensor
def read_temperature():
    try:
        data = I2C_BUS.read_i2c_block_data(I2C_ADDRESS, 0x00, 2)
        temp = (data[0] << 8) | data[1]
        return temp / 16.0
    except Exception as e:
        print(f"Error reading temperature: {e}")
        return None


# Collect data continuously
async def collect_data():
    data = []
    while True:
        temp = read_temperature()
        if temp is not None:
            data.append((datetime.now(), temp))
        await asyncio.sleep(1)
    return data


# Plot collected data
def plot_data(data):
    df = pd.DataFrame(data, columns=["Timestamp", "Temperature"])
    df.set_index("Timestamp", inplace=True)
    df.plot()
    plt.show()


# Store collected data
async def store_data(data):
    df = pd.DataFrame(data, columns=["Timestamp", "Temperature"])
    df.set_index("Timestamp", inplace=True)
    await df.to_csv("temperature_data.csv")


# Main function to read and print temperature
async def main():
    while True:
        temp = read_temperature()
        if temp is not None:
            print(f"Temperature: {temp:.2f}°C")
        await asyncio.sleep(1)


# Run main function if script is executed directly
if __name__ == "__main__":
    asyncio.run(main())
