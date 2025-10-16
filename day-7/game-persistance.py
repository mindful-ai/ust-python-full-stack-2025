import pickle
import time

class Game:

    def __init__(self, player_name, level=1, score=0):
        self.player_name = player_name
        self.level = level
        self.score = score

    def play(self):
        print(f"\n🎯 Welcome {self.player_name}! Starting at Level {self.level}")
        for i in range(3):
            print(f"Playing level {self.level}...")
            time.sleep(1)
            self.score += 10
            self.level += 1
        print(f"✅ Game session ended. Current level: {self.level}, Score: {self.score}")

    def save_game(self, filename="game_save.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self, f)
        print(f"💾 Game saved successfully to {filename}!")

    @staticmethod
    def load_game(filename="game_save.pkl"):
        with open(filename, "rb") as f:
            game = pickle.load(f)
        print(f"🔁 Game loaded successfully from {filename}!")
        return game
    
    #load_game = staticmethod(load_game)

# --------------------------------------------------------------------------------------- #

p1 = Game("Ravi")
p1.play()

p1.save_game()

print("Game Saved! You can resume later...")

loaded_game = Game.load_game()
loaded_game.play()