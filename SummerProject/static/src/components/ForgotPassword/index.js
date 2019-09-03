import React from 'react';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/mainLogInFlow.css';
import '../LogIn/style.css';
import './style.css';


class ForgotPassword extends React.Component {

    render() {
        return (
            <div className="login-page">
                <div className="logo">
                    <Link to="/home" className="logo-link">Sport News</Link>
                </div>
                <div className="log-in">
                    <Link to="/registration/" className="login-link">Don't have an account?</Link>
                    <Link to="/registration/" className="btn btn-primary login login-link">Get Started</Link>
                </div>
                <div className="left-part bg">
                    <img src="/static/imgs/login.jpg" alt="BG"/>
                </div>

                <div className="right-part background">
                    <h1>Forgot your password?</h1>
                    <form className="form">
                        <h3>Enter your email address below and we'll get you back on track</h3>
                        <div className="passw-email">
                            <label>Email address</label>
                            <div className="form-group">
                                <input type="text" placeholder="johndoe@gmail.com" name="email"
                                       className="form-control input-height"/>
                            </div>
                        </div>
                        <div className="sign-up-w">
                            <button type="submit" className="btn-primary sing-up">REQUEST RESENT LINK
                            </button>
                        </div>
                        <div className="log-in-mobile">
                            <Link to="/registration/" className="login-link-mobile">Don't have an account?</Link>
                            <br/>
                            <Link to="/login/" className="login-link-mobile">Back to Sign in</Link>
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

export default ForgotPassword;
