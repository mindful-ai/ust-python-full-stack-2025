# 💻 JavaScript + Knockout.js Assessment  
### **Project Title:** Reactive Calculator Using Knockout.js  

---

## 📝 **Problem Statement**

Create a simple **reactive calculator** web application using **JavaScript** and the **Knockout.js** library.  
The calculator should allow users to enter two numbers and select an operation — **Add**, **Subtract**, **Multiply**, or **Divide** — using **radio buttons**.  

The result should **automatically update** whenever the user changes any input or operation.  
No “Calculate” button should be used.

---

## 🎯 **Requirements**

### **1️⃣ User Interface**
- The page should have:
  - Two **input boxes** for entering operands (e.g., `num1` and `num2`).
  - Four **radio buttons** labeled:
    - Add (+)
    - Subtract (−)
    - Multiply (×)
    - Divide (÷)
  - A **display area** for showing the result dynamically.

### **2️⃣ Behavior**
- Bind all inputs (numbers and operation) to **Knockout observables**.  
- Use a **computed observable** to calculate the result based on the selected operation.  
- The result should update automatically whenever:
  - Either operand changes.
  - The selected operation changes.  
- No explicit button (like “Calculate”) should exist.

---

## 🧠 **Logic Example**

If:
- Operand 1 = `8`
- Operand 2 = `4`
- Operation = `Divide`

Then the displayed result should be:  
👉 **Result: 2**

When the user changes any value or selects another operation, the result updates **instantly**.

---

## 💡 **Hints**
Use Knockout’s `data-bind` attributes for:
- `value:` bindings for input boxes.
- `checked:` binding for radio buttons.
- `text:` binding for result display.


