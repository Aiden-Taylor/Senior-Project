#--------Class file that intitializes the adc
#--------and defines the voltage readout

import board
import digitalio
import busio
import Adafruit_MCP3008


class ADC:

    def __init__(self, channel):
        self.rd_chan = channel

        self.mcp = Adafruit_MCP3008.MCP3008(clk = 23, cs = 15, miso = 21, mosi = 19)

    def readVolts(self):
        #get the adc readout
        adc = self.mcp.read_adc(self.rd_chan)
        return(adc)
