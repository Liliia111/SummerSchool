import React from 'react';
import {Link} from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/mainLogInFlow.css'
import './style.css';


class ResetPassword extends React.Component {

    render() {

        return (
            <div className="login-page">
                <div className="logo">
                    <Link to="/home" className="logo-link">Sport News</Link>
                </div>
                <div className="log-in">
                    <Link to="/registration/" className="login-link">Don't have an account?</Link>
                    <Link to="/registration/" className="btn btn-primary login login-link">Get started</Link>
                </div>
                <div className="left-part bg">
                    <img src="/static/imgs/login.jpg" alt="BG"/>
                </div>

                <div className="right-part background">
                    <h1>Please enter your new password</h1>

                    <form className="form">
                        <div className="passw-email">
                                <label>New password</label>
                                <div>
                                    <div className="form-group">
                                        <input type="password" placeholder="new password" name="password"
                                                className="form-control input-height"/>
                                    </div>
                                </div>
                                <label>Password</label>
                                <div>
                                    <div className="form-group">
                                        <input type="password" placeholder="confrim password" name="password"
                                                className="form-control input-height"/>
                                    </div>
                                </div>
                        </div>
                        <div className="sign-up-w">
                            <button type="submit" className="btn-primary sing-up">SIGN UP
                            </button>
                        </div>
                        <div className="log-in-mobile">
                            <Link to="/registration/" className="login-link-mobile">Don't have an account?</Link>
                        </div>
                        <div className="sign-in">
                            <Link to="/login/" className='sign-in-link'>Back to Sign in</Link>
                        </div>
                    </form>
                </div>
            </div>
        )
    }
}

export default ResetPassword;
