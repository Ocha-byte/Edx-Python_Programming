import asyncio
import time
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
import smbus2


async def main():
    while True:
        temp = read_temperature()
        if temp is not None:
            print(f"Temperature: {temp:.2f}°C")
        await asyncio.sleep(1)


async def read_temperature():
    try:
        bus = smbus2.SMBus(1)
        address = 0x48
        data = bus.read_i2c_block_data(address, 0x00, 2)
        temp = (data[0] << 8 | data[1]) >> 4
        return temp * 0.0625
    except Exception as e:
        print(f"Error reading temperature: {e}")
        return None
