import gyroobj
import pwm
import time
import math


act = pwm.pwm()
gyro = gyroobj.gyroobj()

while True:
    try:
        
        ang = int(input("Give me an angle"))
        run = True
        while run:
            angact = gyro.getFlatAngle()
            
            tol = ang-angact
            
            
            print(tol)
            if abs(tol) < 2:
                run = False
                act.set_speed(0)
            else:
                if ang<angact:
                    print('fuck')
                    act.set_speed(-100)
                else:
                    print('shit')
                    act.set_speed(100)
    except:
        act.set_speed(0)
        break