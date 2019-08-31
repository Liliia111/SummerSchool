/* eslint max-len: ["error", { "ignoreStrings": true }]*/

import React from 'react';
import {Route, Switch, Redirect} from 'react-router-dom';
import Registration from './components/Registration'
import LogIn from './components/LogIn'
import Home from "./components/Home";
import ForgotPassword from "./components/ForgotPassword";


export default class MainRoutes extends React.Component {
  /**
    @return {} - Switch components
   */
  render() {
    return (
      <main id="container">
        <Switch>
          <Route path='/home/' component={Home} />
          <Route path='/registration' component={Registration} />
          <Route path='/login' component={LogIn} />
          <Route path='/forgotPassword' component={ForgotPassword} />
          <Redirect path='*' to='/home/' />
        </Switch>
      </main>
    );
  }
}