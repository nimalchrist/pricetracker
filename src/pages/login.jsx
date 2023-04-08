import React, { useState } from "react";
import "./login.css";

export default function App() {
  const [state, setState] = useState(true);

  const RegisterForm = (
    <form id="Regform">
      <input type="text" placeholder="username" />
      <input type="E-mail" placeholder="Email" />
      <input type="password" placeholder="password" />
      <button type="submit" className="btn">
        Register
      </button>
    </form>
  );

  const LoginForm = (
    <form id="loginform">
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
