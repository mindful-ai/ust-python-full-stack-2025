class Coffee:
    def cost(self):
        return 50

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 10

class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 5

# Client
if __name__ == "__main__":
    basic_coffee = Coffee()
    milk_coffee = MilkDecorator(basic_coffee)
    sugar_milk_coffee = SugarDecorator(milk_coffee)
    print("Total Cost:", sugar_milk_coffee.cost())
