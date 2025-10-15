import random

class WordJumbleGame:

    files = ['words-1.txt', 'words-2.txt']

    def __init__(self, name, level=0):
        self.name = name
        self.points = 0
        self.words = self.fetch_words(WordJumbleGame.files[level])

    def jumble(self, word):
        temp = list(word)
        random.shuffle(temp)
        return ''.join(temp)

    def fetch_words(self, f):
        f = open(f)
        content = f.read()
        f.close()
        return [word.strip() for word in content.split(',')]

    def run(self):
        # for every word in list of words
        random.shuffle(self.words)

        for word in self.words:

            print("\n")

            # jumble the word
            jumbled_word = self.jumble(word)

            # show to the user
            print(jumbled_word)

            # ask user input
            user_word = input("Can you guess -> ")

            # compare user input and update points
            if(user_word == word):
                self.points += 1
                print("\U00002705 Correct")
            else:
                print("\U00002745 In-correct")


    def display_results(self):
        print("\n")
        print(f"NAME  -> {self.name}")
        if (self.points > 6):
            print("You have played well")
        else:
            print("Better luck next time")

# ---------------------------------------------------------------------- #

players = ["Anil", "Sunil", "Vinil"]

objs = [ WordJumbleGame(player) for player in players ]

for obj in objs:
    print(f"PLAYER   -> {getattr(obj, 'name')}")
    obj.run()

print("Displaying Results:")

for obj in objs:
    obj.display_results()