import logo from './logo.svg';
import './App.css';

import React from 'react';
import { useState, useEffect } from 'react';

const WORDS = {
  4: ["GAME", "WORD", "CODE", "MAKE", "TIME", "NODE"],
  5: ["REACT", "PLANT", "BRAVE", "TRAIN", "SMILE"],
  6: ["OBJECT", "PYTHON", "POCKET", "MARKET", "BUTTON"],
};

// Utility to jumble a word
function jumble(word) {
  return word.split("").sort(() => Math.random() - 0.5).join("");
}

// Welcome View
function WelcomeView({ setLevel, startGame }) {
  return (
    <div style={styles.card}>
      <h2>Welcome to Word Jumble!</h2>
      <p>Select your difficulty level:</p>

      <div style={styles.row}>
        <button onClick={() => setLevel(4)}>4 Letter Words</button>
        <button onClick={() => setLevel(5)}>5 Letter Words</button>
        <button onClick={() => setLevel(6)}>6 Letter Words</button>
      </div>

      <button style={styles.startBtn} onClick={startGame}>
        Start Game
      </button>
    </div>
  );
}

// Game View
function GameView({ jumbledWord, answer, setAnswer, checkAnswer, score }) {
  return (
    <div style={styles.card}>
      <h2>Unscramble the Word</h2>
      <h1 style={{ fontSize: "40px", letterSpacing: "6px" }}>{jumbledWord}</h1>

      <input
        placeholder="Your guess..."
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
        style={styles.input}
      />

      <button onClick={checkAnswer}>Submit</button>

      <p>Score: {score}</p>
    </div>
  );
}

// Result View
function ResultView({ history, setView }) {
  return (
    <div style={styles.card}>
      <h2>Your Score History</h2>

      <table border="1" cellPadding="8" style={{ margin: "10px auto" }}>
        <thead>
          <tr>
            <th>Date</th>
            <th>Level</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          {history.map((h, index) => (
            <tr key={index}>
              <td>{h.date}</td>
              <td>{h.level}-letter</td>
              <td>{h.score}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <button onClick={() => setView("welcome")}>Play Again</button>
    </div>
  );
}

function App() {

  const [view, setView] = useState("welcome"); // welcome | game | result
  const [level, setLevel] = useState(null);
  const [word, setWord] = useState("");
  const [jumbledWord, setJumbledWord] = useState("");
  const [answer, setAnswer] = useState("");
  const [score, setScore] = useState(0);
  const [history, setHistory] = useState([]);

  // Load previous scores
  useEffect(() => {
    const saved = JSON.parse(localStorage.getItem("scoreHistory")) || [];
    setHistory(saved);
  }, []);  // Do this once in the beginning

  // Save score when history updates
  useEffect(() => {
    localStorage.setItem("scoreHistory", JSON.stringify(history));
  }, [history]);

  // Start the game
  const startGame = () => {
    const wordList = WORDS[level];
    const selected = wordList[Math.floor(Math.random() * wordList.length)];
    setWord(selected);
    setJumbledWord(jumble(selected));
    setAnswer("");
    setScore(0);
    setView("game");
  };


  // Check the answer
  const checkAnswer = () => {
    if (answer.toUpperCase() === word) {
      setScore(score + 1);

      // Load next word
      const next = WORDS[level][Math.floor(Math.random() * WORDS[level].length)];
      setWord(next);
      setJumbledWord(jumble(next));
      setAnswer("");
    } else {
      // Game ends when the answer is wrong
      const newHistory = [
        ...history,
        { date: new Date().toLocaleString(), level, score },
      ];
      setHistory(newHistory);
      setView("result");
    }
  };

  return (

    <div style={styles.container}>

      {view === "welcome" && (
          <WelcomeView setLevel={setLevel} startGame={startGame} />
      )}

      {view === "game" && (
          <GameView
            jumbledWord={jumbledWord}
            answer={answer}
            setAnswer={setAnswer}
            checkAnswer={checkAnswer}
            score={score}
          />
      )}

      {view === "result" && (
        <ResultView history={history} setView={setView} />
      )}

    </div>
    
  );
}



const styles = {
  container: {
    fontFamily: "Arial",
    textAlign: "center",
    padding: "20px",
  },
  card: {
    padding: "20px",
    maxWidth: "400px",
    margin: "auto",
    borderRadius: "10px",
    border: "1px solid #ccc",
  },
  row: {
    display: "flex",
    justifyContent: "space-around",
    margin: "15px 0",
  },
  startBtn: {
    marginTop: "20px",
    padding: "10px 20px",
  },
  input: {
    padding: "10px",
    margin: "10px",
    width: "80%",
    fontSize: "16px",
  },
};

export default App;
