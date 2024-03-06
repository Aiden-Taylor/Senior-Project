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
        #1/(1/(atan(z/(x^2 + y^2)^(1/2))^2 + atan(y/x)^2))^(1/2)
        self.elevation = math.degrees(1/math.sqrt(1/(pow(math.atan(z/(math.sqrt(pow(x,2) + pow(y,2)))), 2) + pow(math.atan(y/x), 2))))
        angle = self.elevation
        return(angle)
    
    def getCurrAzimuth(self):


        angle = self.accelero.acceleration
        return(angle)