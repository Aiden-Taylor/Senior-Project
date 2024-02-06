#--------Class file that intitializes the adc
#--------and defines the voltage readout

import board
import digitalio
import busio
import adafruit_mcp3xxx.mcp3008
import adafruit_mcp3xxx.analog_in

i2c = board.I2C()

class ADC:
    global rd_chan
    global chan_list

    def __init__(self, channel):
        rd_chan = channel

        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        cs = digitalio.DigitalInOut(board.D5)
        mcp = adafruit_mcp3xxx.mcp3008.MCP3008(spi, cs)
        chan_list = [adafruit_mcp3xxx.analog_in(mcp, adafruit_mcp3xxx.mcp3008.P0), adafruit_mcp3xxx.analog_in(mcp, adafruit_mcp3xxx.mcp3008.P1)]

    def readVolts():
        #get the adc readout
        adc = chan_list[rd_chan].value
        return(adc)
