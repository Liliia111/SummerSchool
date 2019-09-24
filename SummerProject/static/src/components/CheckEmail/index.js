import React from 'react';
import { Link } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/mainLogInFlow.css'
import './style.css';


class CheckEmail extends React.Component {

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
                <div className="backgr-photo bg">
                    <img src="/static/imgs/login.jpg" alt="BG"/>
                </div>
                <div className="main background text-location checkEmail">
                    <div className="mail">
                        <img className="icon-style"/>
                    </div>
                    <h1>Check your email {this.props.location.state.email}</h1>
                    <h4>If there's Sport News account linked to this email address, we'll send over instructions to reset your password.</h4>
                    <div className="log-in-mobile">
                        <Link to="/registration/" className="login-link-mobile">Don't have an account?</Link>
                    </div>
                </div>
            </div>
        )
    }
}

export default CheckEmail;
