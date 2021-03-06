from machine import Pin, I2C
from time import sleep
from bme680 import *

# ESP32 - Pin assignment

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
bme = BME680_I2C(i2c=i2c)

temperatures = [0, 0, 0, 0, 0]
n = 0


def temp_sensor():
    while True:
        print('loop')
        n = 0
        if n >= len(temperatures):
            temperatures[n] = bme.temperature * (9 / 5) + 32

      # temperatures[n] = (((round(bme.temperature * 9/5) + 32.0), 1)

        average = sum(temperatures) / len(temperatures)
        n += 1
        print(round(average, 2))

     # print(average)
     # print(round(temperatures, 2))
     # print("{:.2f}".format(temperatures));

        print(temperatures)
        sleep(10)


temp_sensor()
