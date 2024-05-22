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
minang = -45
maxang = 45
rom = maxang-minang
senscalib = -3


#reading latitude for solar calc
lat = float(input('Enter the Local Latitude: '))
lat = 37.75

#setting the RPi date/time
tim = input('Enter the current time (ex: 2000-01-01 12:34:00): ')
tim = '2024-05-21 15:18:00'
ref0 = (7*3600) + calendar.timegm(time.strptime(tim, '%Y-%m-%d %H:%M:%S')) # the 7 is the timezone
timeref = ref0
currtim = 1 + (timeref - 1704096000)/3600
sttim = currtim
start = time.monotonic()

time_zone = -7
sun = solar.Solar(lat, time_zone)

#getting the northern angle
print('Tell me the angle off north (Measuring from the uphill side).')
north = int(input('my uphill side should be the side with the red control panel: '))
north = 45

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
    try:
        theta = math.degrees(math.asin((zetaprime-zeta)/phi))
    except:
        if (zetaprime > 0):
              theta = maxang
        else:
              theta = minang
    angout = theta
    return(angout)

while True:
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
            curaz -= 180
            desang = computeang(curaz)

            print('Desired follower angle:', desang)
            print()
        time.sleep(.1)
        print(desang)
        desang += senscalib
        actuator.set_angle(desang)
    # except:
        
    #     actuator.set_speed(0)
    #     break
