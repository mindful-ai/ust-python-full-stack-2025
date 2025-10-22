import threading
import random
import time

class WordJumbleGame:
    def __init__(self, words, players):
        self.words = words
        self.players = players
        self.lock = threading.Lock()
        self.current_word = ""
        self.jumbled_word = ""
        self.round_over = False
        self.scores = {p: 0 for p in players}

    def jumble_word(self, word):
        """Return a jumbled version of the word"""
        word_list = list(word)
        random.shuffle(word_list)
        return ''.join(word_list)

    def play_round(self, word):
        """Conduct one round of the game"""
        self.current_word = word
        self.jumbled_word = self.jumble_word(word)
        self.round_over = False

        print(f"\n🌀 Jumbled Word: {self.jumbled_word}")
        print("Players are guessing...\n")

        # Start a thread for each player
        threads = []
        for p in self.players:
            t = threading.Thread(target=self.player_guess, args=(p,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print("Round over!\n")

    def player_activity(self, player_name):
        pass

    def player_guess(self, player_name):
        """Simulate a player trying to guess the word"""
        # Simulate random thinking time
        time.sleep(random.uniform(0.5, 3))

        # Lock to safely check/update shared state
        with self.lock:
            if not self.round_over:
                # Randomly decide if player guessed correctly
                guessed_correct = random.choice([True, False, False])  # lower chance to get correct
                if guessed_correct:
                    print(f"✅ {player_name} guessed it right! The word was '{self.current_word}'.")
                    self.scores[player_name] += 1
                    self.round_over = True
                else:
                    print(f"❌ {player_name} guessed wrong.")

    def show_scores(self):
        """Display current scores"""
        print("\n🏆 Current Scores:")
        for player, score in self.scores.items():
            print(f"{player}: {score}")

    def start_game(self):
        """Start the game with multiple rounds"""
        print("🎮 Starting the Word Jumble Game!\n")
        random.shuffle(self.words)

        for word in self.words:
            self.play_round(word)
            self.show_scores()
            time.sleep(1)

        print("\n🎉 Game Over! Final Scores:")
        self.show_scores()
        winner = max(self.scores, key=self.scores.get)
        print(f"\n🏅 Winner: {winner} 🏅")


# ✅ Example usage
if __name__ == "__main__":
    words = ["python", "multithreading", "decorator", "iterator", "inheritance"]
    players = ["Alice", "Bob", "Charlie", "David"]

    game = WordJumbleGame(words, players)
    game.start_game()
