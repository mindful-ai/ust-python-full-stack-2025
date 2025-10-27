import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data):
        pass

    def sort(self, data):
        pass

    def delete(self, key):
        curr = self.head

        # case: deleting the first node
        if curr and curr.data == key:
            self.head = curr.next
            curr = None
            return
        
        # case: in between
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        # key not found
        if curr is None:
            return
        
        # unlink the node
        prev.next = curr.next
        curr = None

    def display(self):
        
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("\n")

if __name__ == "__main__":

    ll = LinkedList()

    for i in range(10):
        ll.append(random.randint(1, 100))

    ll.display()

    ll.prepend(10)
    ll.prepend(20)
    ll.prepend(30)

    ll.display()

    ll.delete(10)

    ll.display()

