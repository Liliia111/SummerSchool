/* eslint max-len: ["error", { "ignoreStrings": true }]*/

import React from 'react';
import {Route, Switch} from 'react-router-dom';
import Registration from './components/Registration';
import LogIn from './components/LogIn';
import Home from "./components/Home";
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
          <Redirect path='*' to='/home/' />
        </Switch>
      </main>
    );
  }
}