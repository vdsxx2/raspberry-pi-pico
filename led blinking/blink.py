from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)

n = 0

while True:
    led.toggle()
#     print("13 times {} is {}".format(n, 13*n))
#     n = n + 1
    sleep(.5)
