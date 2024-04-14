import serial
import time

ser = serial.Serial('COM6', 115200, timeout=1)
time.sleep(1)  # Give the connection a second to settle

with open('temperature_humidity_data1.csv', 'w') as file:
    while True:
        if ser.in_waiting > 0:
            data_line = ser.readline().decode('utf-8').rstrip()
            file.write(data_line + '\n')
            print(data_line)  # This will also print the data to the console