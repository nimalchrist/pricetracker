import React, { useState } from "react";
import "./login.css";
import { useNavigate } from "react-router-dom";

export default function App() {
  const [state, setState] = useState(true);

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");


  const navigate = useNavigate();

  function handleLogin() {
    // perform login logic here
    // if login is successful, redirect to home page
    navigate("/home");
  }

  const handleRegister = (event) => {
   // navigate("/home");
    event.preventDefault();
  
    // const data = {
    //   username: username,
    //   email: email,
    //   password: password,
    // };
    const data={
      "username": "john",
      "email": "john@example.com",
      "password": "secret"
    }
  
    fetch('/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
        navigate("/home");
        // Handle successful registration here
      })
      .catch((error) => {
        console.error('Error:', error);
        // Handle registration error here
      });
  };
  
   
  

  const RegisterForm = (
    <form id="Regform" onSubmit={handleRegister}>
      <input type="text" placeholder="username" value={username} onChange={(e) => setUsername(e.target.value)} />
<input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
<input type="password" placeholder="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button type="submit" className="btn" onClick={handleRegister}>
        Register
      </button>
    </form>
  );

  const LoginForm = (
    <form id="loginform" onSubmit={handleLogin} >
      <input type="text" placeholder="username" />
      <input type="password" placeholder="password" />
      <button type="submit" className="btn" onClick={handleLogin}>
        Login
      </button>
      <a href="#pass">Forgot password</a>
    </form>
  );

  return (
    <div className="acc-page">
      <div className="form-container">
        <div className="form-btn">
          <span onClick={() => setState(false)}>Login</span>
          <span onClick={() => setState(true)}>Register</span>
          <hr id="indicator" />
          {state ? RegisterForm : LoginForm}
        </div>
      </div>
    </div>
  );
}
