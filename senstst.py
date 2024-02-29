import gyro
import compass

lsm = gyro()
mmc = compass()

while True:
    print(lsm.getAngle())
    print(mmc.getCompass())
