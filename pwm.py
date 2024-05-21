import board
import pwmio
import gyroobj
import RPi.GPIO as GPIO


class pwm:

    def __init__(self):
        self.act_fwd = pwmio.PWMOut(board.D13, frequency=5000, duty_cycle=0)
        self.act_rev = pwmio.PWMOut(board.D12, frequency=5000, duty_cycle=0)
        self.gyro = gyroobj.gyroobj()
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(6, GPIO.OUT)

    def set_speed(self, spd):
        if spd > 0:
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(6, GPIO.HIGH)
            print('setting speed to ' + str(spd))
            self.act_fwd.duty_cycle = 65535*spd/100
            self.act_rev.duty_cycle = 0

        else:
            GPIO.output(5, GPIO.HIGH)
            GPIO.output(6, GPIO.HIGH)

            print('setting speed to ' + str(spd))
            self.act_fwd.duty_cycle = 0
            self.act_rev.duty_cycle = -spd*65535/100

    def set_angle(self, angle):
        ang = angle
        angact = self.gyro.getFlatAngle()
            
        tol = ang-angact
        
        
        #print(tol)
        if (abs(tol) < 1):
            run = False
            self.set_speed(0)
            
        else:
            if tol > 0:
                self.set_speed(-100)
            else:
                self.set_speed(100)    

    def stop(self):
        self.act_fwd.duty_cycle = 0
        self.act_rev.duty_cycle = 0

100
