import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom"

import './App.css';
import { HomePage } from "./pages/HomePage"

const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={HomePage} />
      </Switch>
    </Router>
  )
}

export default App;
