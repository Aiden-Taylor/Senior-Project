import gyroobj
import compass
import time

lsm = gyroobj.gyroobj()
mmc = compass.compass()

while True:
    print(lsm.getAngle())
    print(mmc.getCompass())
    time.sleep(1)
