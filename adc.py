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
        print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*adc))
        return(adc)
