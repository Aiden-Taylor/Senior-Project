import math

class pcontroller:

    def __init__(self, desired, actual, gain):
        self.gain = gain
        self.delta = desired - actual