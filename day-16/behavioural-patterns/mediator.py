# Defines an object that encapsulates how a set of objects interact, promoting loose coupling.

'''
Chat application where users communicate via a central ChatRoom.
'''

class ChatRoom:
    def show_message(self, user, message):
        print(f"[{user}] says: {message}")


class User:
    def __init__(self, name, chatroom):
        self.name = name
        self.chatroom = chatroom

    def send_message(self, message):
        self.chatroom.show_message(self.name, message)


chatroom = ChatRoom()
u1 = User("Alice", chatroom)
u2 = User("Bob", chatroom)

u1.send_message("Hello Bob!")
u2.send_message("Hey Alice!")
