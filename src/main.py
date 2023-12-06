import sys
import board
import busio
from smbus2 import SMBus

i2c = busio.I2C(board.SCL, board.SDA)
print("I2C devices found: ", [hex(i) for i in i2c.scan()])

# Open i2c bus 1 and read one byte from address 7 offset 0
bus = SMBus(bus=1)
b = bus.read_byte_data(i2c_addr=7, register=0)

print(f"bus.read_byte_data: {b}")

b2 = bus.read_block_data(i2c_addr=7, register=0)

print(f"bus.read_block_data: {b2}")

bus.close()
