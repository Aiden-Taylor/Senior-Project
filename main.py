import charger
import gyroobj
import pwm
import adc
import solar
import math
import subprocess
import RPi.GPIO as GPIO
import time

#charger setup so we dont blow everything up
battery = charger.charger()

#setup useful objects
accel = gyroobj.gyroobj()
override = adc.ADC(1)
actuator = pwm.pwm()
GPIO.setup(36, GPIO.IN)

#_____Modify these for our turn limits________
minang = -45
maxang = 45
rom = maxang-minang

#reading latitude for solar calc
lat = input('Enter the Local Latitude: ')

#setting the RPi date/time
tim = input('Enter the current time (YYYY.MM.DD.HH.MM.SS): ')
Y,M,D,h,m,s = tim.split(".")
set_string = Y + "-" + M +"-" + D + " " + h + ":" + m + ":" + s
sudodate = subprocess.Popen(["sudo", "date", "-s", set_string])
sudodate.communicate()

time_zone = -7
sun = solar.Solar(lat, time_zone)

#getting the northern angle
print('Tell me the angle off north (Measuring from the uphill side).')
north = input('my uphill side should be the side with the red control panel: ')

def computeang(azim):
    #calculating the follower angle to match the azimuth
    zeta = math.radians(north)
    zetaprime = math.radians(azim)
    phi = math.radians(accel.getHillAngle())
    theta = math.degrees(math.asin((zetaprime-zeta)/phi))

    angout = theta
    return(angout)

while True:
    try:
        #checking if override is activated
        if (GPIO.input(36) == True):
            print('Override Active')
            outadc = override.readVolts()
            print(outadc)
            desang = outadc*3.3/1024
            desang = (rom*desang/3.3)-45
            
        else:
            currtim = time.time()   #returns in epoch time
            currtim = (currtim-1704096000)/3600 #currtim is number of hours since the start of the year
            curaz = sun.getAzimuth(currtim)
            desang = computeang(curaz)


        actuator.set_angle(desang)
    except:
        
        actuator.set_speed(0)
        break
