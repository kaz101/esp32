import time
import machine

red = machine.Pin(22,machine.Pin.OUT)
for i in range(1):
    red.on()
    time.sleep(1)
    red.off()
    time.sleep(1)
