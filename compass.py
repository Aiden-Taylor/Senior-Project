#--------Class file that intitializes the magnetometer
#--------and defines the compass readout

import board
import adafruit_mmc56x3

i2c = board.I2C()

class compass:
    def __init__(self):
        global magneto
        magneto = adafruit_mmc56x3.MMC5603(i2c)


    def getCompass():
        #get the magnetometer readout

        orientation = magneto.magnetic
        return(orientation)