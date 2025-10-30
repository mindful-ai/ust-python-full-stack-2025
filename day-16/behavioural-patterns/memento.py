# Captures and restores an object’s state without exposing its internals.

class Memento:
    def __init__(self, state):
        self.state = state


class Editor:
    def __init__(self):
        self._text = ""

    def type(self, words):
        self._text += words

    def save(self):
        return Memento(self._text)

    def restore(self, memento):
        self._text = memento.state

    def show(self):
        print(self._text)


editor = Editor()
editor.type("Hello, ")
m1 = editor.save()

editor.type("World!")
m2 = editor.save()

editor.restore(m2)
editor.show()
