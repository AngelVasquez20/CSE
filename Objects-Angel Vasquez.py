class Car(object):
    def __init__(self, power, leather, steel, rubber, color="blue"):
        self.engine = "Jaguar AJ-V8"
        self.leather = leather
        self.steel = steel
        self.rubber = rubber
        self.gas = 100
        self.color = color
        self.functioning = True
        self.power_left = power

    def fill_gas(self, time):
        if self.functioning:
            if self.gas >= 100:
                print("The car is filling up with gas")
                return

            self.power_left += time
            if self.power_left > 100:
                print("The car will fill up in %d" % self.power_left)
                self.power_left = 100
            else:
                print("Your car is now %d low" % self.power_left)
