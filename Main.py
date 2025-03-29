from fPicture import takephoto
from fDecode import decodeimage
from fwavg import wavg
takephoto("testies.jpg")
a = decodeimage("testies.jpg")
print(a)
p = wavg(a)
print(p)