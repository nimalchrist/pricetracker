import React, { useState } from "react";
import "./login.css";
import { useNavigate } from "react-router-dom";

export default function App() {
  const [state, setState] = useState(true);

  const navigate = useNavigate();

  function handleLogin() {
    // perform login logic here
    // if login is successful, redirect to home page
    navigate("/home");
  }

  function handleRegister() {
    // perform login logic here
    // if login is successful, redirect to home page
    navigate("/home");
  }

  const RegisterForm = (
    <form id="Regform" onSubmit={handleRegister}>
      <input type="text" placeholder="username" />
      <input type="E-mail" placeholder="Email" />
      <input type="password" placeholder="password" />
      <button type="submit" className="btn">
        Register
      </button>
    </form>
  );

  const LoginForm = (
    <form id="loginform" onSubmit={handleLogin} >
      <input type="text" placeholder="username" />
      <input type="password" placeholder="password" />
      <button type="submit" className="btn">
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
