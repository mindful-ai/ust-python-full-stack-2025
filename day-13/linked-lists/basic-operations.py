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

    def insert(self, data, pos):
        new_node = Node(data)

        # If the position is at the beginning
        if pos == 0:
            self.prepend(data)
            return
        
        # Move to the desired position
        curr = self.head
        index = 0
        while curr and index < pos - 1:
            curr = curr.next
            index += 1

        # If the position is at the end
        if not curr:
            print("Index out of range")
            self.append(data)
            return
        
        # Otherwise
        new_node.next = curr.next
        curr.next = new_node


    # bubble sort -> simply re-arranging the node links
    def sort(self, key=True):
        # Empty list or only one node -> nothing to sort
        if not self.head or not self.head.next:
            return
        
        end = None
        while end != self.head:
            prev = None
            current = self.head
            while current.next != end:
                next = current.next
                if current.data > next.data:

                    # swapping
                    current.next = next.next
                    next.next = current
                    if prev is None: # if the head is involved in swap
                        self.head = next
                    else:
                        prev.next = next

                    # references should be reset
                    prev = next
                else:
                    prev = current
                    current = current.next
            end = current

                


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

    ll.insert(45, 1)

    ll.display()

    ll.sort()

    ll.display()