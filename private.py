class CoffeeMachine:
    #The machine's max water level is 100, and we want the machine to start if
    #water_level>20
    WATER_LEVER=100


    def start_machine(self):
        if self.WATER_LEVER>20:
            return True

        else
        print("Please add some water!")
        return False


    def boil_water(self):
        #boils the water
        return("boiling...")

    def make_coffee(self):
        if self.start_machine():
            self.WATER_LEVER -=20
            print(self.boil_water())
            print("Your coffee is done!")

machine=CoffeeMachine()
for i in ragne(0,5):
    machine.make_coffee()