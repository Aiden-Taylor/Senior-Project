import gyroobj
import compass
import time

lsm = gyroobj.gyroobj()
mmc = compass.compass()

while True:
    try:
        mag_x, mag_y, mag_z = mmc.getCompass()
        
        #print("X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f}".format(mag_x, mag_y, mag_z))
        print(lsm.getHillAngle())
        time.sleep(1)
    except KeyboardInterrupt:
        break