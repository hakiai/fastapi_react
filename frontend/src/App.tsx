import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom"

import './App.css';
import { HomePage } from "./pages/HomePage"
import { LoginPage } from "./pages/LoginPage"

const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={HomePage} />
      </Switch>
      <Switch>
        <Route path="/login" exact component={LoginPage} />
      </Switch>
    </Router>
  )
}

export default App;
