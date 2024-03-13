import math

class pcontroller:

    def __init__(self, gain):
        self.gain = gain

    def get_effort(self, desired, actual):

        #
        delta = desired - actual
        effort = delta * self.gain

        #saturation
        if effort > 100:
            effort = 100
        else if effort < -100:
            effort = -100
        return(effort)