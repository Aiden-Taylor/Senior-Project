from smbus import SMBus

class charger:

    def __init__(self):
        self.ctrladdr = 0x30
        self.ctrlbus = SMBus(1)
        charge_curr = 0x00
        batt_volt = 0x01

        self.ctrlbus.write_byte_data(self.ctrladdr, batt_volt, 0x0C)
        self.ctrlbus.write_byte_data(self.ctrladdr, charge_curr, 0x01)

    def readPanel(self):
        panel_volt = 0x07
        read = self.ctrlbus.read_byte_data(self.ctrladdr, panel_volt)
        voltage = int(read)*0.141
        return(voltage)