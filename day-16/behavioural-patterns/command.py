# Encapsulates a request as an object, allowing parameterization, queuing, or undo functionality.

class Command:
    def execute(self):
        pass

    def undo(self):
        pass


class TextEditor:
    def __init__(self):
        self.text = ""

    def write(self, content):
        self.text += content

    def erase(self, length):
        self.text = self.text[:-length]


class WriteCommand(Command):
    def __init__(self, editor, content):
        self.editor = editor
        self.content = content

    def execute(self):
        self.editor.write(self.content)

    def undo(self):
        self.editor.erase(len(self.content))


editor = TextEditor()
cmd1 = WriteCommand(editor, "Hello ")
cmd2 = WriteCommand(editor, "World!")

cmd1.execute()
cmd2.execute()
print(editor.text)

cmd2.undo()
print("After undo:", editor.text)
