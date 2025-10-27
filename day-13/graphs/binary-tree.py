class Node:

    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    # Level Order Insertion
    def insert(self, data):
        new_node = Node(data)

        if not self.root:
            self.root = new_node
            return
        
        queue = [self.root]
        while queue:

            current = queue.pop(0)

            if not current.left:
                current.left = new_node
                return
            elif not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.left)
                queue.append(current.right)


    def inorder(self, node):
        if node:    
            self.preorder(node.left)
            print(node.value, end=' ')
            self.preorder(node.right)

    def preorder(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:    
            self.preorder(node.left)
            self.preorder(node.right)
            print(node.value, end=' ')

    def search(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        return self.search(node.left, value) or self.search(node.right, value)


if __name__ == "__main__":

    tree = BinaryTree()
    for val in [10, 3, 4, 5, 7, 2, 3, 7]:
        tree.insert(val)

    print("In order: ")
    tree.inorder(tree.root)

    print("Pre order: ")
    tree.preorder(tree.root)

    print("Post order: ")
    tree.postorder(tree.root)

    print("\nSearching 7:", tree.search(tree.root, 7))
    print("\nSearching 17:", tree.search(tree.root, 17))



