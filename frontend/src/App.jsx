import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import DriverRegister from "./pages/DriverRegister";
import Trips from './pages/Trips';
import './main.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/apply" element={<DriverRegister />} />
        <Route path="/trips" element={<Trips />} />
        <Route path="*" element={<h1>Not Found</h1>} />
      </Routes>
    </Router >
  )
}

export default App