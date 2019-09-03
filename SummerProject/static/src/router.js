/* eslint max-len: ["error", { "ignoreStrings": true }]*/

import React from 'react';
import {Route, Switch, Redirect} from 'react-router-dom';
import Registration from './components/Registration'
import LogIn from './components/LogIn'
import Home from "./components/Home";
import CheckEmail from "./components/CheckEmail"
import ForgotPassword from "./components/ForgotPassword";
import ResetPassword from "./components/ResetPassword";

import ArticlesView from "./components/ArticlesView";
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
          <Route path='/check-email' component={CheckEmail} />
          <Route path='/forgotPassword' component={ForgotPassword} />
          <Route path='/resetPassword' component={ResetPassword}/>
          <Redirect path='*' to='/home/' />
        </Switch>
      </main>
    );
  }
}