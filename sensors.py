import board
import digitalio
import busio
import adafruit_mmc56x3
import adafruit_lsm6ds.lsm6dsox
import adafruit_mcp3xxx.mcp3008
import adafruit_mcp3xxx.analog_in


i2c = board.I2c()
magneto = adafruit_mmc56x3.MMC5603(i2c)
accelero = adafruit_lsm6ds.lsm6dsox.LSM6DSOX(i2c)
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = adafruit_mcp3xxx.mcp3008.MCP3008(spi, cs)
chan_list = [adafruit_mcp3xxx.analog_in(mcp, adafruit_mcp3xxx.mcp3008.P0), adafruit_mcp3xxx.analog_in(mcp, adafruit_mcp3xxx.mcp3008.P1)]

def readVolts(channel):
    #get the adc readout
    adc = chan_list[channel].value
    return(adc)

def getCompass():
    #get the magnetometer readout
    orientation = magneto.magnetic
    return(orientation)

def getAngle():
    #get the accelerometer gyroscopic readout
    angle = accelero.gyro
    return(angle)