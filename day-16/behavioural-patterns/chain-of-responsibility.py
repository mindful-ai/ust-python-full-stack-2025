# Allows a request to pass along a chain of handlers.

class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        raise NotImplementedError


class Level1Support(Handler):
    def handle(self, request):
        if request == "password reset":
            print("Level 1: Handled password reset.")
        elif self._successor:
            self._successor.handle(request)


class Level2Support(Handler):
    def handle(self, request):
        if request == "software installation":
            print("Level 2: Handled software installation.")
        elif self._successor:
            self._successor.handle(request)


class Level3Support(Handler):
    def handle(self, request):
        if request == "server down":
            print("Level 3: Handled server down issue.")
        else:
            print("Issue not handled.")


# Chain setup
chain = Level1Support(Level2Support(Level3Support()))

# Client request
chain.handle("software installation")
chain.handle("server down")
chain.handle("OS issue")
chain.handle("password reset")
