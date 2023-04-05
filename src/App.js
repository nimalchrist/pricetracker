import logo from "./logo.svg";
import "./App.css";
import  { Header } from "./components/Navbar";
import { 
  BrowserRouter as Router,
   Routes
} from 'react-router-dom';

function App() {
  return (
    <Router>
      <Header />
    
  </Router>
  )
}

export default App;
