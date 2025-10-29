# A file system - folders containing files and other folders
# As an other example: consider a switch board consisting of switches, regulators, sockets and fuses

class FileComponent:
    def show_details(self):
        pass

class File(FileComponent):
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"File: {self.name}")

class Folder(FileComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileComponent):
        self.children.append(component)

    def show_details(self):
        print(f"Folder: {self.name}")
        for child in self.children:
            child.show_details()

# Client
if __name__ == "__main__":
    file1 = File("resume.docx")
    file2 = File("photo.jpg")
    subfolder = Folder("Documents")
    subfolder.add(file1)
    subfolder.add(file2)

    main_folder = Folder("Desktop")
    main_folder.add(subfolder)
    main_folder.add(File("notes.txt"))

    main_folder.show_details()
