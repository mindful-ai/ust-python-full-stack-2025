# Allows an object to change its behavior when its internal state changes.

class ATMState:
    def insert_card(self):
        pass


class NoCard(ATMState):
    def insert_card(self):
        print("Card inserted. Please enter PIN.")


class HasCard(ATMState):
    def insert_card(self):
        print("Card already inserted.")


class ATM:
    def __init__(self):
        self.state = NoCard()

    def set_state(self, state):
        self.state = state

    def insert_card(self):
        self.state.insert_card()


atm = ATM()
atm.insert_card()
atm.set_state(HasCard())
atm.insert_card()
