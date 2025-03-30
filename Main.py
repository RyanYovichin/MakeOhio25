from fPicture import takephoto
from fDecode import decodeimage
from fwavg import wavg
from time import sleep
#import serial
g = []
#ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
for i in range(20):
    takephoto("testies.jpg")
    sleep(1)
    a = decodeimage("testies.jpg")
#print(a)
    p = wavg(a)
    g.append(p)
    print(p)
    print()
print(g)
#print(p)