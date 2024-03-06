#--------Class file that intitializes the magnetometer
#--------and defines the compass readout

import board
import adafruit_mmc56x3

i2c = board.I2C()

class compass:
    def __init__(self):
        
        self.magneto = adafruit_mmc56x3.MMC5603(i2c)


    def getCompass(self):
        #get the magnetometer readout

        orientation = self.magneto.magnetic
        return(orientation)
    
    def getNorth(self):
        #should return your angle off of north
        return('fuck, you should probably write this code at some point')