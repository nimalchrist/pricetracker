import React, { useState } from "react";
import "./login.css";
import { useNavigate } from "react-router-dom";

export default function App() {
  const [state, setState] = useState(true);

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMsg, setErrorMsg] = useState("");

  const navigate = useNavigate();

  function handleLogin(event) {
    event.preventDefault();
    const data = {
      email: email,
      password: password,
    };
    fetch("http://localhost:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (response.ok) {
          console.log("Inside the 200 status code");
          navigate("/home");
          // Handle successful registration here
        } else {
          return response.json().then((data) => {
            setErrorMsg(data.msg);
            // Handle registration error here
          });
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        // Handle network error here
        setErrorMsg("Registration failed: " + error.message);
      });
  }

  const handleRegister = (event) => {
    event.preventDefault();

    const data = {
      username: username,
      email: email,
      password: password,
    };
    fetch("http://localhost:5000/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (response.ok) {
          console.log("Inside the 200 status code");
          navigate("/home");
          // Handle successful registration here
        } else {
          return response.json().then((data) => {
            setErrorMsg(data.msg);
            // Handle registration error here
          });
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        // Handle network error here
        setErrorMsg("Registration failed: " + error.message);
      });
  };

  const RegisterForm = (
    <div>
      {errorMsg && (
        <p style={{ color: "red", fontSize: "16px", fontWeight: "bold" }}>
          {errorMsg}
        </p>
      )}
      <form id="RegisterForm" onSubmit={handleRegister}>

        <div class="form-group">

          <input
            class="form-control"
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          /></div>


        <div class="form-group">
          <input
            type="email"
            class="form-control"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          /></div>

        <div class="form-group">
          <input
            class="form-control"
            type="password"
            placeholder="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          /></div>
        <button type="submit" class="btn btn-primary" onClick={handleRegister}>
          Register
        </button>
      </form>
    </div>
  );

  const LoginForm = (
    <div>
      {errorMsg && (
        <p style={{ color: "red", fontSize: "16px", fontWeight: "bold" }}>
          {errorMsg}
        </p>
      )}
      <form id="loginform" onSubmit={handleLogin}>
        <div class="form-group">
          <input
            type="email"
            placeholder="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          /></div>

        <div class="form-group">
          <input
            type="password"
            placeholder="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          /></div>
        <button type="submit" class="btn btn-primary" onClick={handleLogin}>
          Login
        </button>
        <a href="#pass">Forgot password</a>
      </form>
    </div>
  );

  return (
    <div className="acc-page">
      <div className="form-container">
        <div className="form-btn">
          <span onClick={() => setState(false)}>Login</span>
          <span onClick={() => setState(true)}>Register</span>
          {state ? RegisterForm : LoginForm}
        </div>
      </div>
    </div>
  );
}
