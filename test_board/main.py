import time
import machine
import network
import neopixel
from wifi import *

net = network.WLAN(network.STA_IF)
net.active(True)
net.connect(ssid,wifipass)

red = machine.Pin(22,machine.Pin.OUT)
np = neopixel.NeoPixel(machine.Pin(23),121)
for i in range(1):
    red.on()
    time.sleep(1)
    red.off()
    time.sleep(1)
np[120] = (255,0,0)
np.write()
time.sleep(.5)
np[120] = (0,0,0)
np[35] = (0,200,200)
np.write()
for i in range(121):
    np[i] = (0,0,255)
    time.sleep(.02)
    np.write()
    np[i] = (0,0,0)
    time.sleep(.02)
    np.write()
