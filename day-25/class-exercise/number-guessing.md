# 🧮 Assessment: Number Guessing Game

## 🎯 Problem Statement
You are given an **HTML file** for a simple **Number Guessing Game**.  
Your task is to write the JavaScript logic in **`script.js`** to make the game functional.

### Requirements
The game should:

1. Generate a **random number** between **1 and 20** when the page loads.  
2. Allow the user to **guess the number** using an input field.  
3. When the user clicks **“Check Guess”**, compare the input with the generated number and show feedback:
   - “✅ Correct! You guessed it!”  
   - “⬆️ Too high!”  
   - “⬇️ Too low!”  
4. Count the number of **attempts** and show it.  
5. Once guessed correctly, **disable** the input and button.

---

## 🧱 Provided File: `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Number Guessing Game</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-br from-yellow-100 to-green-200 min-h-screen flex flex-col justify-center items-center">
  <div class="bg-white p-8 rounded-2xl shadow-lg text-center w-96">
    <h1 class="text-3xl font-bold text-green-700 mb-6">🔢 Number Guessing Game</h1>

    <p class="text-gray-700 mb-4">Guess the number between <b>1</b> and <b>20</b>.</p>

    <input id="userGuess" type="number" min="1" max="20" placeholder="Enter your guess" class="border p-2 w-full mb-4 text-center rounded-lg" />

    <button onclick="checkGuess()" class="bg-green-600 hover:bg-green-700 text-white w-full py-2 rounded-lg mb-4">Check Guess</button>

    <p id="feedback" class="text-lg font-semibold mb-2"></p>
    <p id="attempts" class="text-sm text-gray-600"></p>
  </div>

  <script src="script.js"></script>
</body>
</html>
```

---

## ✏️ Your Task: Write `script.js`

Implement the following logic:

1. When the page loads:
   - Generate a **random number** between 1 and 20.  
   - Initialize **attempts = 0**.

2. Each time the player clicks **“Check Guess”**:
   - Read the number entered in the input box.  
   - Increment the attempts count.  
   - Compare it with the random number:  
     - If correct → show “✅ Correct! You guessed it!” and disable input and button.  
     - If too high → show “⬇️ Too high! Try again.”  
     - If too low → show “⬆️ Too low! Try again.”  
   - Display the total number of attempts below the feedback.

---

## 🧩 Skeleton Code: `script.js`

```javascript
// Step 1: Generate a random number between 1 and 20
let secretNumber = /* your code here */;
let attempts = 0;

// Step 2: Function to check user's guess
function checkGuess() {
  // Get the user's guess
  const userGuess = /* your code here */;
  
  // Increment attempts
  attempts++;

  // Step 3: Compare guess and give feedback
  if (/* condition for correct guess */) {
    // TODO: Show success message
    // TODO: Disable input and button
  } else if (/* condition for too high */) {
    // TODO: Show "Too high!" message
  } else {
    // TODO: Show "Too low!" message
  }

  // Step 4: Update attempts on screen
  document.getElementById("attempts").textContent = /* your code here */;
}
```

---

## 💡 Expected Output Example

If the secret number is `12`, and the user guesses:
- 8 → “⬆️ Too low! Try again.”  
- 15 → “⬇️ Too high! Try again.”  
- 12 → “✅ Correct! You guessed it in 3 attempts!”

---

**End of Assessment**
