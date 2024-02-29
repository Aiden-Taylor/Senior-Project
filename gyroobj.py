#--------Class file that intitializes the accelerometer
#--------and defines the angle readout

import board
import adafruit_lsm6ds.lsm6dsox

i2c = board.I2C()

class gyroobj:

    def __init__(self):
        
        self.accelero = adafruit_lsm6ds.lsm6dsox.LSM6DSOX(i2c)

    def getAngle(self):
        #get the accelerometer gyroscopic readout


        ###### NEED TO DO CALCULATION TO GET ANGLE FROM GRAVITY VECTOR
        angle = self.accelero.acceleration
        return(angle)