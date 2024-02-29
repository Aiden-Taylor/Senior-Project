import gyroobj
import compass

lsm = gyroobj.gyroobj()
mmc = compass.compass()

while True:
    print(lsm.getAngle())
    print(mmc.getCompass())
