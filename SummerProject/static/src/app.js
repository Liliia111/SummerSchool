import React from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import MuiThemeProvider from "@material-ui/core/styles/MuiThemeProvider";
import MainRoutes from "./router";

const App = () => (
  <Router>
    <MuiThemeProvider>
      <MainRoutes />
    </MuiThemeProvider>
  </Router>
);

render(<App />, document.getElementById("app"));

