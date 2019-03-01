import machine
import bme280

i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
bme = bme280.BME280(i2c=i2c)
t, p, h = bme.values

