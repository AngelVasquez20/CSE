class Car(object):
    def __init__(self, leather, space=82, color="blue"):
        self.engine = "Jaguar AJ-V8"
        self.leather = leather
        self.trunk_space = space
        self.gas = 100
        self.color = color
        self.functioning = True

    def fill_gas(self, time):
        if self.functioning:
            if self.gas >= 100:
                print("The car is already filled up with gas")
                return

            self.gas += time
            if self.gas > 100:
                print("The car will fill up in %d minutes" % self.gas)
                self.gas = 100
            else:
                print("Your car is now %d low" % self.gas)
        else:
            print("Great I have Arrived to my destination!")

    def drive(self):
        self.functioning = False
        print("I took the keys to the car")
        print("Then I drove it to my cousin's house.")

    def use(self, time):
        self.gas -= time
        print("You use the car for %s minutes," % time)


my_car = Car("Black", 82, "blue")

my_car.fill_gas(20)
my_car.use(60)
my_car.drive()
