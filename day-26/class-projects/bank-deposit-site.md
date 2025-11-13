# 💻 Web Development Assessment
### **Project Title:** Simple Bank Deposit Calculator Website  

---

## 📝 **Problem Statement**

Create a **3-page website** for a bank that helps users calculate maturity amounts for **Fixed Deposit (FD)** and **Recurring Deposit (RD)** schemes.

---

## 🌐 **Pages Description**

### **1️⃣ Home Page**
- The home page should welcome the user with a heading such as **“Welcome to Smart Bank Deposits”**.  
- It should contain **two navigation links or buttons**:  
  - **Fixed Deposit Calculator (FD)**  
  - **Recurring Deposit Calculator (RD)**  
- Clicking each button should take the user to the respective calculator page.

---

### **2️⃣ Fixed Deposit (FD) Page**
- Create a **form** that allows users to enter details for FD calculation using:
  - **Principal Amount** (input box or range slider)  
  - **Rate of Interest (per annum)** (input box or range slider)  
  - **Time Period (in years)** (input box or range slider)  
- Include a **“Calculate”** button.  
- On clicking the button, the **maturity value** should be displayed below the form.  

**Formula for FD Maturity:**  
\[
A = P \times \left(1 + \frac{R}{100}\right)^T
\]  
where:  
- \( A \) = Maturity Amount  
- \( P \) = Principal Amount  
- \( R \) = Rate of Interest  
- \( T \) = Time in years  

---

### **3️⃣ Recurring Deposit (RD) Page**
- Create a **form** that allows users to enter:
  - **Monthly Deposit Amount** (input box or range slider)  
  - **Rate of Interest (per annum)** (input box or range slider)  
  - **Time Period (in months)** (input box or range slider)  
- Include a **“Calculate”** button.  
- On clicking the button, display the **maturity value** below the form.

**Formula for RD Maturity:**  
\[
A = P \times \frac{(1 + R/400)^N - 1}{1 - (1 + R/400)^{-1/3}}
\]  
where:  
- \( A \) = Maturity Amount  
- \( P \) = Monthly Deposit  
- \( R \) = Rate of Interest  
- \( N \) = Number of months  

---

## 🧭 **Navigation**
- Each page should have a navigation bar or links to move between:
  - **Home**
  - **FD Calculator**
  - **RD Calculator**

---

## 🎯 **Expected Output**
- Clean, user-friendly design.
- Responsive form inputs with sliders.
- Correct calculation and display of results.
- Functional navigation between pages.
