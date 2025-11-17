
# React Assessment: Guess My Number Game

## Objective
Build a simple but fully functional **Guess My Number** game using **React functional components and hooks**.

---

## Requirements

### 1. Three Views / Screens

#### **Welcome View**
- Shows the title of the game.
- Lets the user choose a difficulty level:
  - Easy → 1 to 20
  - Medium → 1 to 50
  - Hard → 1 to 100
- Includes a “Start Game” button.

#### **Game View**
- Randomly generates a secret number based on the difficulty.
- Allows user to enter a guess.
- Displays hints:
  - **Too High!**
  - **Too Low!**
  - **Correct!**
- Track the number of attempts.
- On correct guess → navigate to Result View.

#### **Result View**
- Shows:
  - Difficulty selected
  - Secret number
  - Attempts taken
- Displays **table of previous game results**.
- Stores results using **localStorage**.
- Includes a **Play Again** button.

---

## Mandatory Features
- Use **React Hooks** (`useState`, `useEffect`).
- Use **localStorage** to store results history.
- Clean, reusable components.
- Use props for data passing.
- Simple, clear UI (no frameworks required).

---

## Score History Format

Each game result must be stored as:

```json
{
  "date": "12/02/2025, 10:32 AM",
  "difficulty": "Easy",
  "attempts": 7
}
```

---

## Rules
- User cannot enter numbers outside the allowed range.
- Game ends only when correct guess is entered.
- Optional enhancements:
  - Sound effects
  - Emoji feedback
  - Animations
  - Reset button for clearing history

---

## Deliverables
Students must submit:
1. Working React application
2. Source code (App.js + components)
3. Screenshot/video showing:
   - Welcome View
   - Game View
   - Results View with history

---

Good luck and have fun building the game!
