# Allows adding new operations to objects without modifying their structure.

class Item:
    def accept(self, visitor):
        pass


class Book(Item):
    def accept(self, visitor):
        visitor.visit_book(self)


class Food(Item):
    def accept(self, visitor):
        visitor.visit_food(self)


class TaxVisitor:
    def visit_book(self, book):
        print("Book tax: 5%")

    def visit_food(self, food):
        print("Food tax: 10%")


items = [Book(), Food()]
visitor = TaxVisitor()

for item in items:
    item.accept(visitor)
