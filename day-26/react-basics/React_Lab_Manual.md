# ⚛️ React Lab Manual
### Workshop: Understanding Virtual DOM, Components, Events, and State in React

---

## 🧩 Lab #1.1 – Creating Virtual DOM Trees

**Notes:**  
React provides a way to construct Virtual DOM trees that describe what the browser’s DOM should look like. When React updates, it compares these virtual representations and efficiently updates only the parts that change.

This allows us to **describe what the UI should look like**, not how to update it.

**➡️ index.js**
```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';

const vdom = React.createElement(
  'p', // a <p> element
  { className: 'big' }, // with class="big"
  'Hello World!' // and the text
);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(vdom);
```

---

## 🧩 Lab #1.2 – Creating Virtual DOM Trees using JSX

JSX lets us write HTML-like syntax in JavaScript. Tools like Babel compile JSX into `React.createElement()` calls.

**➡️ index.js**
```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';

const vdom = <p className="big">Hello World!</p>;

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(vdom);
```

---

## 🧩 Lab #1.3 – Using Expressions in JSX

You can use JavaScript expressions inside JSX by wrapping them in `{}`.

**➡️ index.js**
```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';

const maybeBig = Math.random() > 0.5 ? 'big' : 'small';
const vdom = <p className={maybeBig}>Hello {40 + 2}!</p>;

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(vdom);
```

---

## 🧩 Lab #1.4 – Using Function Definitions

The `style` prop in React uses a JavaScript object.

**➡️ App.js**
```jsx
import React from 'react';

function App() {
  return (
    <p className="big" style={{ color: 'purple' }}>
      Hello <em>World</em>!
    </p>
  );
}

export default App;
```

**➡️ index.js**
```jsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
```

---

## 🧪 Lab #2 – Events

Event handlers in React are registered declaratively as props, prefixed with `on`.

**➡️ App.js**
```jsx
import React, { useState } from 'react';

function App() {
  const [count, setCount] = useState(0);

  const clicked = () => {
    setCount(count + 1);
    console.log('Clicked ' + count);
  };

  return (
    <div>
      <h3 className="count">Count: {count}</h3>
      <button onClick={clicked}>Click Me!</button>
    </div>
  );
}

export default App;
```

---

## 🧩 Lab #3 – Components

A **Component** is a reusable part of the UI that can receive inputs (props) and return JSX.

**➡️ App.js**
```jsx
import React from 'react';

function MyButton(props) {
  return <button className="my-button">{props.text}</button>;
}

export default function App() {
  return <MyButton text="Click Me!" />;
}
```

---

## 🧩 Lab #3.1 – Nesting Components

**➡️ App.js**
```jsx
import React from 'react';

function MyButton(props) {
  return <button className="my-button">{props.text}</button>;
}

function MediaPlayer(props) {
  return (
    <div>
      {props.playing ? <MyButton text="Stop" /> : <MyButton text="Play" />}
    </div>
  );
}

export default function App() {
  return <MediaPlayer playing={false} />;
}
```

---

## 🧩 Lab #3.2 – Component Children

**➡️ App.js**
```jsx
import React from 'react';

function MyButton(props) {
  return <button className="my-button">{props.children}</button>;
}

function App() {
  return (
    <MyButton>
      <img src="icon.png" alt="icon" /> Click Me!
    </MyButton>
  );
}

export default App;
```

---

## 🧩 Lab #3.3 – Component Classes

Class components can use lifecycle methods such as `componentDidMount` and `componentDidUpdate`.

**➡️ App.js**
```jsx
import React, { Component } from 'react';

class MyButton extends Component {
  componentDidMount() {
    console.log('Hello from a new <MyButton> component!');
  }

  componentDidUpdate() {
    console.log('A <MyButton> component was updated!');
  }

  render() {
    return <button className="my-button">{this.props.children}</button>;
  }
}

export default function App() {
  return <MyButton>Click Me!</MyButton>;
}
```

---

## 🧩 Lab #3.4 – Practical Component Example

**➡️ App.js**
```jsx
import React from 'react';

function MyButton(props) {
  return (
    <button style={props.style} onClick={props.onClick}>
      {props.children}
    </button>
  );
}

export default function App() {
  const clicked = () => console.log('Hello!');

  return (
    <div>
      <p className="count">Count:</p>
      <MyButton style={{ color: 'purple' }} onClick={clicked}>
        Click me
      </MyButton>
    </div>
  );
}
```

---

## 🧩 Lab #4 – State in React

State allows components to store and update dynamic data.

---

### 🧩 Lab #4.1 – State in Class Components

**➡️ App.js**
```jsx
import React, { Component } from 'react';

class MyButton extends Component {
  state = { clicked: false };

  handleClick = () => {
    this.setState({ clicked: true });
  };

  render() {
    return (
      <button onClick={this.handleClick}>
        {this.state.clicked ? 'Clicked' : 'No clicks yet'}
      </button>
    );
  }
}

export default MyButton;
```

---

### 🧩 Lab #4.2 – State in Function Components with Hooks

**➡️ App.js**
```jsx
import React, { useState } from 'react';

function MyButton() {
  const [clicked, setClicked] = useState(false);

  const handleClick = () => {
    setClicked(true);
  };

  return (
    <button onClick={handleClick}>
      {clicked ? 'Clicked' : 'No clicks yet'}
    </button>
  );
}

export default MyButton;
```

---

### 🧩 Lab #4.3 – Practical: Counter Example

**➡️ App.js**
```jsx
import React, { useState } from 'react';

function MyButton(props) {
  return (
    <button style={props.style} onClick={props.onClick}>
      {props.children}
    </button>
  );
}

function App() {
  const [count, setCount] = useState(0);

  const clicked = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <p className="count">Count: {count}</p>
      <MyButton style={{ color: 'purple' }} onClick={clicked}>
        Click me
      </MyButton>
    </div>
  );
}

export default App;
```

---

## 🏁 Conclusion

✅ Learned about Virtual DOM in React  
✅ Created and rendered components  
✅ Handled props and state  
✅ Registered event handlers declaratively  
✅ Used functional and class components  

Congratulations — you’ve completed your **React Lab Manual**! ⚛️🎉
