#--------Class file that intitializes the accelerometer
#--------and defines the angle readout

import board
import adafruit_lsm6ds.lsm6dsox

i2c = board.I2C()

class gyro:

    def __init__(self):
        global accelero
        accelero = adafruit_lsm6ds.lsm6dsox.LSM6DSOX(i2c)

    def getAngle():
        #get the accelerometer gyroscopic readout

        angle = accelero.gyro
        return(angle)