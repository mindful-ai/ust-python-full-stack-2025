const words = ["apple", "tiger", "crown", "bread", "house", "grape", "lemon", "river"]
let currentWordIndex = 0;
let score = 0;

function shuffleWord(word){
    return word.split('').sort( () => Math.random() - 0.5 ).join('');
}

function showWord(){
    const jumbled = shuffleWord(words[currentWordIndex]);
    document.getElementById('jumbledWord').textContent = jumbled;
    document.getElementById('userInput').textContent = '';
    document.getElementById('feedback').textContent = '';
    document.getElementById('progress').textContent = `Word ${currentWordIndex + 1} of ${words.length}`

}

function checkAnswer(){

    // Get the user guess
    const userGuess = document.getElementById("userInput").value.trim().toLowerCase();
    if(!userGuess) return;

    // Compare and update the score
    if (userGuess == words[currentWordIndex]){
        score++;
        document.getElementById("feedback").textContent = "✅ Correct";
        document.getElementById("feedback").className = "text-green-600 mt-4 text-lg font-semibold";
    }
    else {
        document.getElementById("feedback").textContent = `❌ Wrong! ${words[currentWordIndex]}`;
        document.getElementById("feedback").className = "text-red-600 mt-4 text-lg font-semibold";
    }

    // Move to the word
    currentWordIndex++;
    if(currentWordIndex < words.length){
        setTimeout(showWord, 1000);
    } else {
        localStorage.setItem("finalScore", score);
        window.location.href = "result.html"
    }

}

if(window.location.pathname.includes("game.html")){
    showWord();
}
