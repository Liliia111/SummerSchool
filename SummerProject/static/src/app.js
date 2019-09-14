import React from 'react';
import {render} from 'react-dom';
import {BrowserRouter as Router, Route, Link} from "react-router-dom";
import createMuiTheme from "@material-ui/core/styles/createMuiTheme";
import MuiThemeProvider from '@material-ui/core/styles/MuiThemeProvider';
import MainRoutes from './router';

const theme = createMuiTheme();
const App = () => (
    <Router>
        <MuiThemeProvider theme={theme}>
            <MainRoutes/>
        </MuiThemeProvider>
    </Router>
);

render(<App />, document.getElementById("app"));

