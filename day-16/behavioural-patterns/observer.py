# Defines a one-to-many dependency so that when one object changes state, all dependents are notified.

class Observer:
    def update(self, price):
        pass


class Stock:
    def __init__(self):
        self._observers = []
        self._price = 0

    def attach(self, observer):
        self._observers.append(observer)

    def set_price(self, price):
        self._price = price
        self._notify_all()

    def _notify_all(self):
        for obs in self._observers:
            obs.update(self._price)


class Investor(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, price):
        print(f"{self.name} notified. New stock price: {price}")


stock = Stock()
stock.attach(Investor("Anil"))
stock.attach(Investor("Sunil"))

stock.set_price(120)
