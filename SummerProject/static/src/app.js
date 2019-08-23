import React from 'react';
import {render} from 'react-dom';
import {BrowserRouter as Router} from 'react-router-dom';
import MuiThemeProvider from '@material-ui/core/styles/MuiThemeProvider';

import Header from './components/Header/';
import MainRouter from './router';

const Footer = () => <div>Footer Will be implemented soon</div>;

const App = () => (
  <Router>
    <MuiThemeProvider>
      <Header/>
        <MainRouter/>
      <Footer/>
    </MuiThemeProvider>
  </Router>
);

render(<App />, document.getElementById('app'));
