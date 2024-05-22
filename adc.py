#--------Class file that intitializes the adc
#--------and defines the voltage readout

import board
import digitalio
import busio
import Adafruit_MCP3008


class ADC:

    def __init__(self, channel):
        self.rd_chan = channel

        self.mcp = Adafruit_MCP3008.MCP3008(clk = 11, cs = 22, miso = 9, mosi = 10)

    def readVolts(self):
        #get the adc readout
        adc = self.mcp.read_adc(self.rd_chan)
        return(adc)
