import sys
import board
import busio
from smbus2 import SMBus

I2C_ADDRESS = 7
SENSOR_ADDRESS = 0x7

# Detect i2c devices
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C devices found: ", [hex(i) for i in i2c.scan()])


# Print error when sensor not found
if not SENSOR_ADDRESS in i2c.scan():
    print(f"Could not find fs2012 device at {SENSOR_ADDRESS}")
    print("sys.exit()")
    sys.exit()


# Open i2c bus 1 and read one byte from address 7 offset 0
bus = SMBus(bus=1)
b = bus.read_byte_data(i2c_addr=7, register=0)

print(f"bus.read_byte_data: {b}")

b2 = bus.read_block_data(i2c_addr=7, register=0)

print(f"bus.read_block_data: {b2}")


write1 = bus.i2c_msg.write(I2C_ADDRESS, list1)
write2 = bus.i2c_msg.write(I2C_ADDRESS, list2)

num_bytes = 4
read = bus.i2c_msg.read(I2C_ADDRESS, num_bytes)

bus.i2c_rdwr(write1, write2, read)
data = list(read)
print(data)

bus.close()
