import charger
import gyroobj
import pwm
import adc
import solar
import math

override = adc.ADC(1)
while True:
    override.readVolts