from abc import ABC

class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print('Consuming tea')

class Coffe(HotDrink):
    def consume(self):
        print('Consuming coffe')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'prepared {amount} of tea')
        return Tea()

class CoffeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'prepared {amount} of coffe')
        return Coffe()
