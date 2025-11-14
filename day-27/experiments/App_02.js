import React from "react";
import { useState } from "react";


export default function App() {

    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [gender, setGender] = useState("");
    const [skills, setSkills] = useState([]);

    const handleSubmit = (e) => {

        e.preventDefault(); // Prevent page reload
        console.log(e);
        alert(`Name: ${name}\nEmail: ${email}\nGender: ${gender}\nSkills: ${skills.join(", ")}`);

    }

    const handleSkillsChanged = (e) => {

        const value = e.target.value;

        // If the skill already exists - user unchecks the box
        if( skills.includes(value) ){
            setSkills(skills.filter((skill) => skill != value))
        }

        // Otherwise add - user checks the box
        else {
            setSkills([...skills, value]);  // skills[:].append(value)
        }
    }

    return(
        <div style={{ width: "500px", margin: "20px auto"}}>

            <h2>React Form Demonstration</h2>

            <form onSubmit={ handleSubmit }>

                {/* Name Field */}
                <div style={{ marginBottom: "10px" }}>
                    <label>Name: </label><br />
                    <input  type="text" 
                            value={name} 
                            onChange={ (e) => setName(e.target.value) }
                            placeholder="Enter your name"
                    />
                </div>
                {/* Email Field */}
                <div style={{ marginBottom: "10px" }}>
                    <label>Email: </label><br />
                    <input  type="email" 
                            value={email} 
                            onChange={ (e) => setEmail(e.target.value) }
                            placeholder="Enter your name"
                    />
                </div>
                {/* Gender Radio Buttons */}
                <div>
                    <label>Gender</label><br />
                    <label>
                        <input  type="radio" 
                                name="gender"
                                value="Male"
                                onChange={ (e) => setGender(e.target.value) }
                                checked={gender === "Male"}
                        /> Male
                    </label><br />
                    <label>
                        <input  type="radio" 
                                name="gender"
                                value="Female"
                                onChange={ (e) => setGender(e.target.value) }
                                checked={gender === "Female"}
                        /> Female
                    </label><br />
                    <label>
                        <input  type="radio" 
                                name="gender"
                                value="Other"
                                onChange={ (e) => setGender(e.target.value) }
                                checked={gender === "Other"}
                        /> Other
                    </label><br />
                </div>
                {/* Skills Check Boxes */}
                <div>
                    <label>Skills</label><br />
                    <label>
                        <input  type="checkbox" 
                                value="Javascript"
                                onChange={ handleSkillsChanged }
                                checked={ skills.includes("Javascript") }
                        /> Javascript
                    </label><br />
                    <label>
                        <input  type="checkbox" 
                                value="HTML"
                                onChange={ handleSkillsChanged }
                                checked={ skills.includes("HTML") }
                        /> HTML
                    </label><br />
                    <label>
                        <input  type="checkbox" 
                                value="CSS"
                                onChange={ handleSkillsChanged }
                                checked={ skills.includes("CSS") }
                        /> CSS
                    </label><br />
                    <label>
                        <input  type="checkbox" 
                                value="React"
                                onChange={ handleSkillsChanged }
                                checked={ skills.includes("React") }
                        /> React
                    </label><br />
                </div>

                <button type="submit">Submit</button>

            </form>

        </div>
    )


}

// export default App;