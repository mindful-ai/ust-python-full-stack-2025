# 🧠 Workshop Manual: Installing and Creating Your First Project in React Framework

---

## 🗓️ Objective

By the end of this workshop, you will be able to:

✅ Install and set up **React**  
✅ Understand **Virtual DOM** and how React updates it efficiently  
✅ Build React **components** (functional and class-based)  
✅ Manage **state** and **props**  
✅ Handle **events** and user input  
✅ Build and run your first React project

---

## ⚙️ 1. Prerequisites

- Node.js (v16 or above)  
- npm or yarn  
- Code editor (VS Code recommended)  
- Basic knowledge of HTML, CSS, and JavaScript  

---

## 🚀 2. Step 1 – Install Node.js and npm

Download and install from [https://nodejs.org](https://nodejs.org)

Verify installation:

```bash
node -v
npm -v
```

---

## ⚛️ 3. Step 2 – Create Your First React Project

You can create a React app using **Create React App**:

```bash
npx create-react-app my-first-react-app
```

Move into the folder and start the development server:

```bash
cd my-first-react-app
npm start
```

It will open `http://localhost:3000/` in your browser.

---

## 🧩 4. Step 3 – Project Structure Overview

```
my-first-react-app/
├── node_modules/
├── public/
│   └── index.html
├── src/
│   ├── App.js
│   ├── index.js
│   └── App.css
└── package.json
```

The key files are:

- `index.js` — Entry point, renders `<App />` to the DOM  
- `App.js` — Main component where you write UI code  

---

## 🧠 5. Step 4 – Understanding Virtual DOM

React maintains a **virtual representation of the DOM** in memory.  
When something changes, it updates only the affected parts of the real DOM.

Example:

```jsx
const element = <h1>Hello React!</h1>;
ReactDOM.render(element, document.getElementById('root'));
```

---

## 🧩 6. Step 5 – Create Your First Component

### Functional Component

```jsx
function Welcome() {
  return <h2>Welcome to React Workshop!</h2>;
}

export default Welcome;
```

Include it inside `App.js`:

```jsx
import Welcome from './Welcome';

function App() {
  return (
    <div>
      <Welcome />
    </div>
  );
}

export default App;
```

---

## 🧮 7. Step 6 – Working with Props

Props are inputs to components.

```jsx
function Greet(props) {
  return <h3>Hello, {props.name}!</h3>;
}

export default Greet;
```

Usage:

```jsx
<Greet name="Student" />
```

---

## 🔁 8. Step 7 – Managing State with Hooks

React provides `useState()` hook for managing component state.

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}

export default Counter;
```

Use in `App.js`:

```jsx
import Counter from './Counter';

function App() {
  return (
    <div>
      <h1>React State Example</h1>
      <Counter />
    </div>
  );
}
```

---

## 🎯 9. Step 8 – Handling Events

React events are camelCase and receive event objects.

```jsx
function ClickButton() {
  function handleClick() {
    alert('Button Clicked!');
  }

  return <button onClick={handleClick}>Click Me</button>;
}
```

Include in your `App.js`:

```jsx
import ClickButton from './ClickButton';
```

---

## 🧱 10. Step 9 – Combining Components

```jsx
import Greet from './Greet';
import Counter from './Counter';
import ClickButton from './ClickButton';

function App() {
  return (
    <div>
      <Greet name="React Learner" />
      <ClickButton />
      <Counter />
    </div>
  );
}

export default App;
```

---

## 🧪 11. Step 10 – Experiments and Labs

### 🧩 Experiment 1: Virtual DOM Update

Modify `App.js`:

```jsx
function App() {
  const element = <h1>Time: {new Date().toLocaleTimeString()}</h1>;
  return element;
}
```

Then set an interval in `index.js`:

```jsx
import ReactDOM from 'react-dom/client';
import App from './App';

setInterval(() => {
  ReactDOM.createRoot(document.getElementById('root')).render(<App />);
}, 1000);
```

---

### 🧩 Experiment 2: Functional Component and Props

```jsx
function Message(props) {
  return <h2>{props.text}</h2>;
}

function App() {
  return <Message text="React makes UI interactive!" />;
}
```

---

### 🧩 Experiment 3: useState and Events

```jsx
import { useState } from 'react';

function ToggleMessage() {
  const [show, setShow] = useState(true);

  return (
    <div>
      <button onClick={() => setShow(!show)}>
        {show ? 'Hide' : 'Show'}
      </button>
      {show && <p>Hello React World!</p>}
    </div>
  );
}

export default ToggleMessage;
```

Include in App:

```jsx
import ToggleMessage from './ToggleMessage';

function App() {
  return <ToggleMessage />;
}
```

---

### 🧩 Experiment 4: Class Component (Optional)

```jsx
import React from 'react';

class Welcome extends React.Component {
  render() {
    return <h2>Hello from Class Component!</h2>;
  }
}

export default Welcome;
```

Include in App:

```jsx
import Welcome from './Welcome';

function App() {
  return <Welcome />;
}
```

---

## 🏁 Conclusion

You have successfully:

✅ Installed React  
✅ Created and rendered components  
✅ Used props and state  
✅ Handled events  
✅ Understood Virtual DOM  

Congratulations! You’ve built your **first React project** 🎉
