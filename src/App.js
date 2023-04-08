import "./App.css";
import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
import Loginswitch from "./pages/login";

function App() {
  return (
    <Router>
      <Loginswitch />
    </Router>
  );
}

export default App;
