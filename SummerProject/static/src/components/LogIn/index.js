import React from 'react';
import {Link} from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/mainLogInFlow.css'
import './style.css';
import axios from '../../axios';


class Login extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            email: '',
            password: '',
            error: false,
        }
    }

    changeHandler = event => {
        this.setState({[event.target.name]: event.target.value})
    };

    submitHandler = event => {
        event.preventDefault();
        axios
            .post('/api/v1/user/login/', {
                'email': this.state.email,
                'password': this.state.password,
            })
            .then(() => {
                this.props.history.push('/home')
            })
            .catch(() => {
                this.setState({error: true})
            })
    };


    render() {
        const {email, password} = this.state;
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
                    <h1>Log in to Sport News</h1>
                    <form onSubmit={this.submitHandler} className="form">
                        <div className="passw-email">
                            <label>Email address</label>
                            <div className="form-group">
                                <input type="text" placeholder="johndoe@gmail.com" name="email" value={email}
                                       onChange={this.changeHandler}
                                       className="form-control input-height"/>
                            </div>
                            <div className="password">
                                <label>Password</label>
                                <Link to="/forgotPassword" className="password-link">Forgot password?</Link>
                            </div>
                            <div>
                                <div className="form-group">
                                    <input type="password" placeholder="4 + caharacters" name="password"
                                           value={password} onChange={this.changeHandler}
                                           className="form-control input-height"/>
                                </div>
                            </div>
                        </div>
                        <div className="sign-up-w">
                            <button type="submit" onClick={this.submitHandler} className="btn-primary sing-up">LOG IN
                            </button>
                        </div>
                        {
                            this.state.error && <div className="help-block">
                                Invalid login or password
                            </div>
                        }
                        <div className="log-in-mobile">
                            <Link to="/registration/" className="login-link-mobile">Don't have an account?</Link>
                        </div>
                    </form>
                </div>
            </div>
        )
    }
}

export default Login;
