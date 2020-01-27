class CoffeeTooHot(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class CoffeeTooCold(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class CoffeeCup:

    def __init__(self,temperature):
        self.temp=temperature

    def drinkCoffee(self):
        if self.temp>60:
            raise CoffeeTooHot("Coffee too hot")
        elif self.temp<20:
            raise CoffeeTooCold("Coffee too cold")
        else:
            print("Coffee is ok to drink")

cup= CoffeeCup(523)
try:
    cup.drinkCoffee()
except Exception as e:
    print(e)