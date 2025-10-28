class FileNode:
    def __init__(self, name, is_directory=False):
        self.name = name
        self.is_directory = is_directory
        self.children = []  # Only used if it's a directory

    def add_child(self, child_node):
        if self.is_directory:
            self.children.append(child_node)
        else:
            raise Exception(f"Cannot add child to file: {self.name}")

    def display(self, level=0):
        prefix = "📁 " if self.is_directory else "📄 "
        print("   " * level + prefix + self.name)
        for child in self.children:
            child.display(level + 1)


# Building a sample file system
root = FileNode("root", is_directory=True)

# Subdirectories
home = FileNode("home", is_directory=True)
user = FileNode("user", is_directory=True)
docs = FileNode("documents", is_directory=True)
pics = FileNode("pictures", is_directory=True)

# Files
file1 = FileNode("resume.pdf")
file2 = FileNode("project.py")
file3 = FileNode("photo.jpg")
file4 = FileNode("notes.txt")

# Construct the tree
root.add_child(home)
home.add_child(user)
user.add_child(docs)
user.add_child(pics)

docs.add_child(file1)
docs.add_child(file2)
pics.add_child(file3)
user.add_child(file4)

# Display the file system hierarchy
root.display()
