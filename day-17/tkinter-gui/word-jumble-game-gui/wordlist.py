import random

# A simple list of words for the game
WORDS = [
    "python", "variable", "function", "loop", "string",
    "integer", "boolean", "tuple", "dictionary", "class",
    "object", "inheritance", "encapsulation", "module", "package"
]

def get_jumbled_word():
    """Returns a random word and its jumbled version."""
    word = random.choice(WORDS)
    jumbled = ''.join(random.sample(word, len(word)))
    return word, jumbled
