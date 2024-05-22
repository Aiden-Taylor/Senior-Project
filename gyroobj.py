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
        # -- Below formula is from a derivation in Aiden's SP Notebook, with
        # -- MatLab used to solve it for phi.
        #1/(1/(atan(z/(x^2 + y^2)^(1/2))^2 + atan(y/x)^2))^(1/2)
        try:
            full = math.sqrt(pow(x,2) + pow(y,2) + pow(z,2))
            #z = math.sqrt(pow(z,2) + pow(y,2))
            self.elevation = math.acos(x/full)
            self.elevation = 90 - math.degrees(self.elevation)
            #self.elevation = 90 - math.degrees(1/math.sqrt(1/(pow(math.atan(z/(math.sqrt(pow(x,2) + pow(y,2)))), 2) + pow(math.atan(y/x), 2))))
        except:
            self.elevation = 0
        return(self.elevation)
    
    def getFlatAngle(self):
        x, y, z = self.accelero.acceleration
        try:
            self.theta = math.atan(y/z)
            self.theta = math.degrees(self.theta)
            if self.theta < 0:
                self.theta = (self.theta + 90)
            else:
                self.theta = (self.theta - 90)
        except:
            self.theta = 90
        return(self.theta)

    def getCurrAngle(self):
        x, y, z = self.accelero.acceleration
        try:
            self.theta = math.asin(math.atan(y/z)/self.getHillAngle())
            self.theta = -1*math.degrees(self.theta)
        except:
            self.theta = 90
        return(self.theta)

    def getCurrAzimuth(self, north):

        self.azim = north + self.getHillAngle()*math.sin(self.getCurrAngle())
        return(self.azim)
    
    def getRaw(self):
        x, y, z = self.accelero.acceleration
        return(x,y,z)