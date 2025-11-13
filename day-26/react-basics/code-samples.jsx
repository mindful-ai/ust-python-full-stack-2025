import React from 'react';
import ReactDOM from 'react-dom/client';

const vdom = React.createElement(
  'p',                 // element type
  { className: 'big' }, // attributes
  'Hello World!'        // children
);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(vdom);

// ---------------------------------------------------------------------------------------------------------
import React from 'react';
import ReactDOM from 'react-dom/client';

const vdom = <p className="big">Hello World!</p>;

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(vdom);


// ---------------------------------------------------------------------------------------------------------

import React from 'react';
import ReactDOM from 'react-dom/client';

const maybeBig = Math.random() > 0.5 ? 'big' : 'small';
const vdom = <p className={maybeBig}>Hello {40 + 2}!</p>;

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(vdom);




// ---------------------------------------------------------------------------------------------------------

import React from 'react';
import ReactDOM from 'react-dom/client';

function App() {
  return (
    <p className="big" style={{ color: 'purple' }}>
      Hello <em>World</em>!
    </p>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);



// ---------------------------------------------------------------------------------------------------------


import React from 'react';
import ReactDOM from 'react-dom/client';

function App() {
  let i = 0;

  const clicked = () => {
    i += 1;
    console.log('Hi ' + i);
  };

  return (
    <div>
      <h3 className="count">Count: {i}</h3>
      <button onClick={clicked}>Click Me!</button>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);


// ---------------------------------------------------------------------------------------------------------


function MyButton(props) {
  return <button className="my-button">{props.text}</button>;
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyButton text="Click Me!" />);


// ---------------------------------------------------------------------------------------------------------


function MyButton(props) {
  return <button>{props.text}</button>;
}

function MediaPlayer() {
  return (
    <div>
      <MyButton text="Play" />
      <MyButton text="Stop" />
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MediaPlayer />);


// ---------------------------------------------------------------------------------------------------------

function MediaPlayer(props) {
  return (
    <div>
      {props.playing ? (
        <MyButton text="Stop" />
      ) : (
        <MyButton text="Play" />
      )}
    </div>
  );
}

root.render(<MediaPlayer playing={false} />);



// ---------------------------------------------------------------------------------------------------------

function MyButton(props) {
  return <button className="my-button">{props.children}</button>;
}

function App() {
  return (
    <MyButton>
      <img src="icon.png" alt="icon" />
      Click Me!
    </MyButton>
  );
}

root.render(<App />);




// ---------------------------------------------------------------------------------------------------------



import React, { Component } from 'react';
import ReactDOM from 'react-dom/client';

class MyButton extends Component {
  render() {
    return <button>{this.props.children}</button>;
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyButton>Click Me!</MyButton>);


// ---------------------------------------------------------------------------------------------------------


class MyButton extends React.Component {
  componentDidMount() {
    console.log('Mounted!');
  }

  componentDidUpdate() {
    console.log('Updated!');
  }

  render() {
    return <button>{this.props.children}</button>;
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyButton>Click Me!</MyButton>);


// ---------------------------------------------------------------------------------------------------------


function MyButton(props) {
  return (
    <button style={props.style} onClick={props.onClick}>
      {props.children}
    </button>
  );
}

function App() {
  const clicked = () => {
    console.log('Hello!');
  };

  return (
    <div>
      <p className="count">Count:</p>
      <MyButton style={{ color: 'purple' }} onClick={clicked}>
        Click me
      </MyButton>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);



// ---------------------------------------------------------------------------------------------------------

class MyButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { clicked: false };
  }

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


// ---------------------------------------------------------------------------------------------------------


import React, { useState } from 'react';

function MyButton() {
  const [clicked, setClicked] = useState(false);

  const handleClick = () => setClicked(true);

  return (
    <button onClick={handleClick}>
      {clicked ? 'Clicked' : 'No clicks yet'}
    </button>
  );
}


// ---------------------------------------------------------------------------------------------------------

import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';

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

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);



// ---------------------------------------------------------------------------------------------------------




// ---------------------------------------------------------------------------------------------------------



// ---------------------------------------------------------------------------------------------------------




// ---------------------------------------------------------------------------------------------------------