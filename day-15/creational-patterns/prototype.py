# Help you clone or copy existing objects instead of creating new ones

import copy

# Prototype Interface
class Prototype:
    def clone(self):
        return copy.deepcopy(self)


# Concrete Class
class Document(Prototype):
    def __init__(self, title, content, author, template_type):
        self.title = title
        self.content = content
        self.author = author
        self.template_type = template_type

    def __str__(self):
        return (f"Document: {self.title}\n"
                f"Type: {self.template_type}\n"
                f"Author: {self.author}\n"
                f"Content: {self.content}\n")


# Client Code
if __name__ == "__main__":
    # Create a base prototype (template)
    offer_template = Document(
        title="Offer Letter Template",
        content="Dear [Name], we are pleased to offer you the position of [Role] at [Company].",
        author="HR Department",
        template_type="Offer Letter"
    )

    # Clone and customize for a new employee
    offer_john = offer_template.clone()
    offer_john.title = "Offer Letter - John Doe"
    offer_john.content = offer_john.content.replace("[Name]", "John Doe").replace("[Role]", "Software Engineer").replace("[Company]", "TechNova Ltd.")

    # Another customized version
    offer_jane = offer_template.clone()
    offer_jane.title = "Offer Letter - Jane Smith"
    offer_jane.content = offer_jane.content.replace("[Name]", "Jane Smith").replace("[Role]", "Data Scientist").replace("[Company]", "TechNova Ltd.")

    print(offer_template)
    print("----------")
    print(offer_john)
    print("----------")
    print(offer_jane)
