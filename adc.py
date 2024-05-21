#--------Class file that intitializes the adc
#--------and defines the voltage readout

import board
import digitalio
import busio
import adafruit_mcp3xxx.mcp3008
import adafruit_mcp3xxx.analog_in

i2c = board.I2C()

class ADC:

    def __init__(self, channel):
        self.rd_chan = channel

        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        cs = digitalio.DigitalInOut(board.D22)
        mcp = adafruit_mcp3xxx.mcp3008.MCP3008(spi, cs)
        self.chan_list = [adafruit_mcp3xxx.analog_in(mcp, adafruit_mcp3xxx.mcp3008.P0), adafruit_mcp3xxx.analog_in(mcp, adafruit_mcp3xxx.mcp3008.P1)]

    def readVolts(self):
        #get the adc readout
        adc = self.chan_list[self.rd_chan].value
        return(adc)
