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
        
        #print("X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f}".format(mag_x, mag_y, mag_z))
        print(lsm.getCurrAzimuth(25))
        time.sleep(1)
    except KeyboardInterrupt:
        break