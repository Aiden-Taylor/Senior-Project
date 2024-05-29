from smbus import SMBus

class charger:

    def __init__(self):
        self.ctrladdr = 0x30
        self.ctrlbus = SMBus(1)
        charge_curr = 0x00
        batt_volt = 0x01

        try:
            self.ctrlbus.write_byte_data(self.ctrladdr, batt_volt, 0x0C)
            self.ctrlbus.write_byte_data(self.ctrladdr, charge_curr, 0x01)
        except Exception as e:
            print(e)
    def readPanel(self):
        try:
            panel_volt = 0x07
            read = self.ctrlbus.read_word_data(self.ctrladdr, panel_volt)
            print(read)
            read = int(read[9:16], 2)
            voltage = read*0.141
            return(voltage)
        except Exception as e:
            print(e)
            voltage = 6969
            return(voltage)