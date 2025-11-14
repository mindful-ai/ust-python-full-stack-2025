import React, { useState } from "react";

export default function App(){

    // keep inputs as strings for controlled inputs and validate on calculate
    const [num1, setNum1] = useState("");
    const [num2, setNum2] = useState("");
    const [operation, setOperation] = useState("add");
    const [result, setResult] = useState("");

    
    const calculate = () => {
        const a = parseFloat(num1);
        const b = parseFloat(num2);

        if (Number.isNaN(a) || Number.isNaN(b)) {
            setResult("Error: invalid number");
            return;
        }

        let res;
        switch (operation) {
            case "add":
                res = a + b;
                break;
            case "sub":
                res = a - b;
                break;
            case "mul":
                res = a * b;
                break;
            case "div":
                res = b === 0 ? "Error: Division by zero" : a / b;
                break;
            default:
                res = "Invalid operation";
        }

        setResult(res);
    };
    

    return(

        <div>
            
            <h2>Calculator Using React</h2>

            <div>

                <label>Operand A: </label>
                <input  type="number"
                        placeholder="Enter number 1"
                        value={num1}
                        onChange={(e) => setNum1(e.target.value)}
                /><br />
                <label>Operand B: </label>
                <input  type="number"
                        placeholder="Enter number 2"
                        value={num2}
                        onChange={(e) => setNum2(e.target.value)}
                /><br />

                {/* Operations Radio Buttons */}
                <div>
                    <label>Operations</label><br />
                    <label>
                        <input  type="radio" 
                            name="op"
                            value="add"
                            onChange={ (e) => setOperation(e.target.value) }
                            checked={operation === "add"}
                        /> Add
                    </label><br />
                    <label>
                        <input  type="radio" 
                            name="op"
                            value="sub"
                            onChange={ (e) => setOperation(e.target.value) }
                            checked={operation === "sub"}
                        /> Subtract
                    </label><br />
                    <label>
                        <input  type="radio" 
                            name="op"
                            value="mul"
                            onChange={ (e) => setOperation(e.target.value) }
                            checked={operation === "mul"}
                        /> Multiply
                    </label><br />
                    <label>
                        <input  type="radio" 
                            name="op"
                            value="div"
                            onChange={ (e) => setOperation(e.target.value) }
                            checked={operation === "div"}
                        /> Divide
                    </label><br />
                </div>

                {/* Calculate Button */}
                <button onClick={calculate}>Calculate</button>

                {/* Result Display */}
                <h3>Result: {result}</h3>

            </div>
        
        </div>

    )
}