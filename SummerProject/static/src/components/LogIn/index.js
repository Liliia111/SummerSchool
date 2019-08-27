import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/mainLogInFlow.css'
import './style.css';
import axios from 'axios';



const API_URL = 'http://localhost:8000';


class Login extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            email: '',
            password: '',
        }
    }

    changeHandler = event => {
        this.setState({[event.target.name]: event.target.value})
    };

    submitHandler = event => {
        event.preventDefault()
        console.log(this.state);
        axios
            .post(API_URL + '/api/v1/user/login/', {
                'email': this.state.email,
                'password': this.state.password,
            })
            .then(response => {
                console.log(response)
                console.log(response.data)
            })
            .catch(error => {
                console.log(error)
            })
    };


    render() {
        const {email, password} = this.state;
        return (
            <div className="login-page">
                <div className="logo">
                    <a href="http://localhost:8000/home/">Sport News</a>
                </div>
                <div className="log-in">
                    <a href="http://localhost:8000/registration/">Don't have an account?</a>
                    <a href="http://localhost:8000/registration/" className="btn btn-primary login">Get Started</a>
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
                                <a href="#fgpsw">Forgot password?</a>
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
                        <div className="log-in-mobile">
                            <a href="http://localhost:8000/registration/">Don't have an account?</a>
                        </div>
                    </form>
                </div>
            </div>
        )
    }
}

export default Login;
