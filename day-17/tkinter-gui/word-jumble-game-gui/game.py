import tkinter as tk
from tkinter import messagebox
from wordlist import get_jumbled_word

class WordJumbleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Jumble Game")
        self.root.geometry("400x300")
        self.root.config(bg="#f0f0f0")

        # Game state variables
        self.original_word = ""
        self.jumbled_word = ""
        self.score = 0

        # UI Elements
        self.title_label = tk.Label(root, text="🔤 Word Jumble Game", font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.word_label = tk.Label(root, text="", font=("Helvetica", 22, "bold"), fg="blue", bg="#f0f0f0")
        self.word_label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)

        self.submit_btn = tk.Button(root, text="Submit", font=("Arial", 12, "bold"), command=self.check_word)
        self.submit_btn.pack(pady=5)

        self.next_btn = tk.Button(root, text="Next Word", font=("Arial", 12, "bold"), command=self.new_word)
        self.next_btn.pack(pady=5)

        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 12), bg="#f0f0f0")
        self.score_label.pack(pady=10)

        self.new_word()

    def new_word(self):
        """Fetches a new word and updates the display."""
        self.original_word, self.jumbled_word = get_jumbled_word()
        self.word_label.config(text=self.jumbled_word)
        self.entry.delete(0, tk.END)

    def check_word(self):
        """Checks if the entered word matches the original."""
        user_word = self.entry.get().strip().lower()
        if user_word == self.original_word:
            self.score += 1
            messagebox.showinfo("Correct!", f"✅ Correct! The word was '{self.original_word}'.")
        else:
            messagebox.showwarning("Wrong!", f"❌ Wrong! The correct word was '{self.original_word}'.")
        self.score_label.config(text=f"Score: {self.score}")
        self.new_word()

if __name__ == "__main__":
    root = tk.Tk()
    app = WordJumbleGame(root)
    root.mainloop()
