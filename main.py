import charger
import gyroobj
import pwm
import adc
import solar
import math
import subprocess
import RPi.GPIO as GPIO
import board
import time
import calendar
from os import system

#charger setup so we dont blow everything up
battery = charger.charger()
#start = time.monotonic()

#setup useful objects
accel = gyroobj.gyroobj()
override = adc.ADC(0)
actuator = pwm.pwm()
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)

#_____Modify these for our turn limits________
minang = -65
maxang = 46
rom = maxang-minang
senscalib = -3


#reading latitude for solar calc
latfile = open('/home/aiden/Senior-Project/lat.txt', 'r')
lat = float(latfile.readline())
# print(lat)
# lat = float(input('Enter the Local Latitude: '))
# lat = 35.1819

#setting the RPi date/time
dat = open('/home/aiden/Senior-Project/time.txt', 'r')
tim = dat.readline()
tim = tim[0:19]
# print(tim)
dat.close()

# tim = input('Enter the current time (ex: 2000-01-01 12:34:00): ')
# tim = '2024-05-23 12:22:00'
ref0 = (7*3600) + calendar.timegm(time.strptime(tim, '%Y-%m-%d %H:%M:%S')) # the 7 is the timezone
timeref = ref0
currtim = 1 + (timeref - 1704096000)/3600
sttim = currtim
start = time.monotonic()

time_zone = -7
sun = solar.Solar(lat, time_zone)

#getting the northern angle
# print('Tell me the angle off north (Measuring from the uphill side).')
# print('Express angles in -180:0:180 domain.')
# north = int(input('my uphill side should be the side with the red control panel: '))
north = float(latfile.readline())
latfile.close()
# print(north)

def computeang(azim):
    #calculating the follower angle to match the azimuth
    zeta = math.radians(north)
    zetaprime = math.radians(azim)
    phi = math.radians(accel.getHillAngle())
    # phi = math.radians(45)
    # print('azim: ' + str(math.degrees(azim)))
    # print('zeta: ' + str(math.degrees(zeta)))
    # print('  zp: ' + str(math.degrees(zetaprime)))
    # print(' phi: ' + str(math.degrees(phi)))
    # try:
        #theta = math.degrees(math.asin((zetaprime-zeta)/phi))
    zetaprime = azim - north
    theta = .5*(zetaprime - 180)
    if theta > maxang:
        theta = maxang
    elif theta < minang:
            theta = minang
    # except:
    #     if (zetaprime > 0):
    #           theta = maxang
    #     else:
    #           theta = minang
    angout = -theta
    return(angout)

while True:
        # system('clear')
    #try:
        # checking if override is activated
        if (GPIO.input(16) == False):
            
            print('Override Active')
            outadc = override.readVolts()
            print(outadc)
            desang = (outadc-512)/1024
            desang = (rom*desang)

        # if override not active:    
        else:
            
            rn = (time.monotonic()-start)/3600
            currtim = sttim + rn   #smart?
            #print('seconds' + str(currtim))
            timeref = ref0 + rn*3600
            print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(timeref)))
            #currtim is number of hours since the start of the year
            curaz = sun.getAzimuth(currtim)
            print()
            print('       Current azimuth:', curaz)
            desang = computeang(curaz)

            
        
        print('Desired follower angle:', desang)
        print('Panel Output: ', battery.readPanel())
        desang += senscalib
        actuator.set_angle(desang)
        time.sleep(.1)
    # except:
        
    #     actuator.set_speed(0)
    #     break
