#--------Class file that intitializes the accelerometer
#--------and defines the angle readout

import board
import adafruit_lsm6ds.lsm6dsox
import math

i2c = board.I2C()

class gyroobj:

    def __init__(self):
        
        self.accelero = adafruit_lsm6ds.lsm6dsox.LSM6DSOX(i2c)

    def getHillAngle(self):
        #THIS ASSUMES THAT THE X AXIS IS ALIGNED WITH THE PANEL PIVOT AXIS

        x, y, z = self.accelero.acceleration
        self.zenith = math.degrees(math.atan(y/x))
        self.elevation = 1/(1/(math.atan(z/(x^2 + y^2)^(1/2))^2 + math.atan(y/x)^2))^(1/2)
        angle = self.elevation
        return(angle)
    
    def getCurrAzimuth(self):


        angle = self.accelero.acceleration
        return(angle)