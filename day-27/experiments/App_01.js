import logo from './logo.svg';
import './App.css';
import { useState } from "react";


function ButtonComponent(props){
  return(
    <button style={props.buttonStyle} onClick={props.buttonClick}>
      {props.children}
    </button>
  )
}

function App() {

  let i = 0;
  let myColor = "red";

  const [value, setValue] = useState(0);
  const [color, setColor] = useState("red");

  const clicked = () => {
    i += 1;
    setValue(value + 1);
    myColor = Math.random() > 0.5 ? "red" : "blue";
    setColor(myColor)
    console.log('I = ' + i + 'COLOR = ' + myColor);
  }

  return (
    <div className='App-header'>
      <h3>Clicked ({value}) times!</h3>
      <strong><p className="big" style={{color:color}}>Hello React World! {45 + 56}</p></strong>
      <ButtonComponent buttonStyle={{color: 'green'}} buttonClick={clicked}>CLICK ME!</ButtonComponent>
    </div>
  );
}

export default App;
