import gyroobj
import compass

lsm = gyroobj()
mmc = compass()

while True:
    print(lsm.getAngle())
    print(mmc.getCompass())
