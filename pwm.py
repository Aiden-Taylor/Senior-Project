import board
import pwmio
import RPi.GPIO as GPIO




class pwm:
    
    def __init__(self):
        self.act_fwd = pwmio.PWMOut(board.D18, frequency=5000, duty_cycle=0)
        self.act_rev = pwmio.PWMOut(board.D12, frequency=5000, duty_cycle=0)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(8, GPIO.OUT)

    def set_speed(self, spd):
        if spd > 0:
            GPIO.OUT(7, GPIO.HIGH)
            GPIO.OUT(board.D8, GPIO.LOW)

            self.act_fwd.duty_cycle = spd
            self.act_rev.duty_cycle = 0

        else:
            GPIO.OUT(7, GPIO.LOW)
            GPIO.OUT(board.D8, GPIO.HIGH)

            self.act_fwd.duty_cycle = 0
            self.act_rev.duty_cycle = -spd
