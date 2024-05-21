import board
import pwmio
import RPi.GPIO as GPIO


class pwm:

    def __init__(self):
        self.act_fwd = pwmio.PWMOut(board.D13, frequency=5000, duty_cycle=0)
        self.act_rev = pwmio.PWMOut(board.D12, frequency=5000, duty_cycle=0)
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

    def stop(self):
        self.act_fwd.duty_cycle = 0
        self.act_rev.duty_cycle = 0

100
