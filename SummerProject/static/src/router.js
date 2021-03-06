/* eslint max-len: ["error", { "ignoreStrings": true }]*/

import React from 'react';
import {Route, Switch, Redirect} from 'react-router-dom';
import Registration from './components/Registration'
import LogIn from './components/LogIn'
import Home from "./components/Home";
import Articles from "./components/Articles";
import Video from "./components/Video";
import CheckEmail from "./components/CheckEmail"
import ForgotPassword from "./components/ForgotPassword";
import ResetPassword from "./components/ResetPassword";
import Comments from "./components/Comments";
import CommentsComp from "./components/CommentsComp";
import PersonalInfo from "./components/PersonalInfo"

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
          <Route path='/articles/:id' component={Articles} />
          <Route path='/videos/:id' component={Video} />
          <Route path='/check-email' component={CheckEmail} />
          <Route path='/forgotPassword' component={ForgotPassword} />
          <Route path='/resetPassword' component={ResetPassword}/>
          <Route path='/comments' component={Comments}/>
          <Route path='/commentsComp' component={CommentsComp}/>
          <Route path='/personalInfo' component={PersonalInfo}/>
          <Redirect path='*' to='/home/' />
        </Switch>
      </main>
    );
  }
}