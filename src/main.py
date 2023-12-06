import sys
import board
import busio
from smbus2 import SMBus

SENSOR_ADDRESS = 0x7

# Detect i2c devices
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C devices found: ", [hex(i) for i in i2c.scan()])


# Print error when sensor not found
if not SENSOR_ADDRESS in i2c.scan():
    print(f"Could not find fs2012 device at {SENSOR_ADDRESS}")

# Open i2c bus 1 and read one byte from address 7 offset 0
bus = SMBus(bus=1)
b = bus.read_byte_data(i2c_addr=7, register=0)

print(f"bus.read_byte_data: {b}")

b2 = bus.read_block_data(i2c_addr=7, register=0)

print(f"bus.read_block_data: {b2}")

bus.close()
