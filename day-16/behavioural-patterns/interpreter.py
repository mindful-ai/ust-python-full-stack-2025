# Defines a grammatical representation for a language and an interpreter to evaluate sentences in the language.

class Expression:
    def interpret(self):
        pass


class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value


class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()


# Expression: (5 + 10)
expr = Add(Number(5), Number(10))
print("Result:", expr.interpret())
