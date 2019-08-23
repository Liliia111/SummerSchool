/* eslint max-len: ["error", { "ignoreStrings": true }]*/

import React from 'react';
import {Route, Switch, Redirect} from 'react-router-dom';
import Registration from './components/Registration'

const Home =()=><div>Home</div>

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
          <Redirect path='*' to='/home/' />
        </Switch>
      </main>
    );
  }
}