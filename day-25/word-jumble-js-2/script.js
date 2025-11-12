const words = ["apple", "tiger", "lemon", "grape", "chair", "plane", "house", "river", "bread", "crown"];
let currentWordIndex = 0;
let score = 0;
let timer;
let timeLeft = 15;

function shuffleWord(word) {
  return word.split('').sort(() => Math.random() - 0.5).join('');
}

function showWord() {
  // Reset timer
  clearInterval(timer);
  timeLeft = 15;
  document.getElementById("timer").textContent = timeLeft;

  // Show next jumbled word
  const jumbled = shuffleWord(words[currentWordIndex]);
  document.getElementById("jumbledWord").textContent = jumbled;
  document.getElementById("userInput").value = "";
  document.getElementById("feedback").textContent = "";
  document.getElementById("progress").textContent = `Word ${currentWordIndex + 1} of ${words.length}`;

  // Start countdown
  timer = setInterval(() => {
    timeLeft--;
    document.getElementById("timer").textContent = timeLeft;

    if (timeLeft <= 0) {
      clearInterval(timer);
      document.getElementById("feedback").textContent = `⏰ Time's up! Correct word: ${words[currentWordIndex]}`;
      document.getElementById("feedback").className = "text-red-600 mt-4 text-lg font-semibold";
      nextWord();
    }
  }, 1000);
}

function checkAnswer() {
  const userGuess = document.getElementById("userInput").value.trim().toLowerCase();
  if (!userGuess) return;

  clearInterval(timer);

  if (userGuess === words[currentWordIndex]) {
    score++;
    document.getElementById("feedback").textContent = "✅ Correct!";
    document.getElementById("feedback").className = "text-green-600 mt-4 text-lg font-semibold";
  } else {
    document.getElementById("feedback").textContent = `❌ Wrong! (${words[currentWordIndex]})`;
    document.getElementById("feedback").className = "text-red-600 mt-4 text-lg font-semibold";
  }

  nextWord();
}

function nextWord() {
  currentWordIndex++;
  if (currentWordIndex < words.length) {
    setTimeout(showWord, 1000);
  } else {
    endGame();
  }
}

function endGame() {
  localStorage.setItem("finalScore", score);
  window.location.href = "result.html";
}

// When on game page
if (window.location.pathname.includes("game.html")) {
  showWord();
}
