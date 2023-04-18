import "./App.css";
import React from "react";
import { BrowserRouter as Router, Routes,Route,Navigate } from "react-router-dom";
import Loginswitch from "./pages/login";
import Home from "./pages/HomePage"

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Loginswitch />} />
        <Route path="/home" element={<Home />} />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </Router>
  );
}

export default App;
