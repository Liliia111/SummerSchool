import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './style.css';


class Registration extends React.Component {
    render() {
        return (
            <div className="login-page">
                <div className="logo">
                    <a href="#logo">Sport News</a>
                </div>
                <div className="log-in">
                    <a href="#">Already have an account?</a>
                    <a href="#" className="btn btn-primary login">Log In</a>
                </div>
                <div className="left-part bg">
                    <img src="/static/imgs/login.jpg" alt="BG"/>
                </div>

                <div className="right-part background">
                    <h1>Create Account</h1>
                    <p>Or use your email for registration:</p>
                    <div className="user-data">
                        <div className="form-group">
                            <label>First Name</label>
                            <input type="text" placeholder="John" name="first_name" className="form-control"/>
                        </div>
                        <div className="form-group ">
                            <label>Last Name</label>
                            <input type="text" placeholder="Doe" name="last_name" className="form-control"/>
                        </div>
                    </div>
                    <div className="passw-email">
                        <label>Email</label>
                        <div className="form-group">
                            <input type="text" placeholder="johndoe@gmail.com" name="email"
                                   className="form-control input-height"/>
                        </div>
                        <label>Password</label>
                        <div>
                            <div className="form-group">
                                <input type="password" placeholder="4 + caharacters" name="password"
                                       className="form-control input-height"/>
                            </div>
                        </div>
                    </div>
                    <div className="sign-up-w">
                        <button type="submit" className="btn-primary sing-up">SIGN UP</button>
                    </div>
                </div>
            </div>
        )
    }
}

export default Registration;
