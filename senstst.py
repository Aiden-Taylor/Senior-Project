import gyroobj
import compass
import pwm
import time

lsm = gyroobj.gyroobj()
mmc = compass.compass()


# actuator = pwm.pwm()

# actuator.set_speed(100)
# time.sleep(1)
# actuator.set_speed(0)
while True:
    try:
        mag_x, mag_y, mag_z = mmc.getCompass()
        print("Magnetometer Output:")
        print("X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f}".format(mag_x, mag_y, mag_z))
        print()
        print("Orientation to North: ")
        print(lsm.getCurrAzimuth(25))
        print()
        print("Hill Angle: ")
        print(lsm.getHillAngle())
        print()
        time.sleep(2)
    except KeyboardInterrupt:
        break