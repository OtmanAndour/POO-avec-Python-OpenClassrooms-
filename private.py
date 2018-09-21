class CoffeeMachine:
    #The machine's max water level is 100, and we want the machine to start if
    #water_level>20
    WATER_LEVER=100


    def _start_machine(self): #Adding an underscore before start_machine means that this method is now protected
        if self.WATER_LEVER>20:
            return True

        else:
            print("Please add some water!")
            return False


    def __boil_water(self): #Adding 2 underscores before boil_water means that this method is now private
        #boils the water
        return("boiling...")

    def make_coffee(self):
        if self._start_machine():
            self.WATER_LEVER -=20
            print(self.__boil_water())
            print("Your coffee is done!")

machine=CoffeeMachine()
#for i in range(0,5):
#    machine.make_coffee()
print("Make coffee:Public", machine.make_coffee())
print("Start machine:Protected",machine._start_machine())
print("Boil water:Private", machine._CoffeeMachine__boil_water())