import React from 'react';
import {Link, Redirect} from 'react-router-dom'
import FacebookLogin from 'react-facebook-login';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/mainLogInFlow.css'
import './style.css';
import axios from '../../axios';
import FormValidator from '../../validator/FormValidator';
import {rules} from './validation_rules'


class Registration extends React.Component {
    constructor(props) {
        super(props);

        this.validator = new FormValidator(rules);

        this.state = {
            firstName: '',
            lastName: '',
            email: '',
            password: '',
            validation: this.validator.valid(),
            error: false,
        };
    }

    changeHandler = event => {
        this.setState({[event.target.name]: event.target.value})
    };

    submitHandler = event => {
        event.preventDefault();
        const validation = this.validator.validate(this.state);
        this.setState({validation});
        this.submitted = true;

        if (validation.isValid) {
            axios
                .post('/api/v1/user/registration/', {
                    'first_name': this.state.firstName,
                    'last_name': this.state.lastName,
                    'email': this.state.email,
                    'password': this.state.password,
                })
                .then(() => {
                    this.props.history.push('/login')
                })
                .catch(() => {
                    this.setState({error: true})
                })
        }
    };

    responseFacebook(response) {
        axios
            .post('/api/v1/user/facebookRegistration/', {
                'first_name': response.first_name,
                'last_name': response.last_name,
                'userId': response.id,
            });
        window.location = '/home';
    };

    render() {
        const {firstName, lastName, email, password} = this.state;
        let validation = this.submitted ?
            this.validator.validate(this.state) :
            this.state.validation;

        return (
            <div className="login-page">
                <div className="logo">
                    <Link to="/home" className="logo-link">Sport News</Link>
                </div>
                <div className="log-in">
                    <Link to="/login/" className="login-link">Already have an account?</Link>
                    <Link to="/login/" className="btn btn-primary login login-link">Login</Link>
                </div>
                <div className="left-part bg">
                    <img src="/static/imgs/login.jpg" alt="BG"/>
                </div>

                <div className="right-part background">
                    <h1>Create Account</h1>
                    <div className="link-button">
                        <div className="social-log">
                            <FacebookLogin
                                appId="674638763014681"
                                autoLoad={false}
                                fields="email, first_name, last_name"
                                callback={this.responseFacebook}
                            />
                        </div>
                        <div className="googl">
                            <a href="#" className="gg">
                                <img className="icon-style"/>
                            </a>
                        </div>
                    </div>
                    <p>Or use your email for registration:</p>
                    <form className="form">
                        <div className="user-data">
                            <div className="form-group">
                                <div className={validation.firstName.isInvalid && 'has-error'}>
                                    <label>First Name</label>
                                    <input type="text" placeholder="John" name="firstName" value={firstName}
                                           onChange={this.changeHandler} className="form-control"/>
                                    <span className="help-block">{validation.firstName.message}</span>
                                </div>
                            </div>
                            <div className="form-group ">
                                <div className={validation.lastName.isInvalid && 'has-error'}>
                                    <label>Last Name</label>
                                    <input type="text" placeholder="Doe" name="lastName" value={lastName}
                                           onChange={this.changeHandler} className="form-control"/>
                                    <span className="help-block">{validation.lastName.message}</span>
                                </div>
                            </div>
                        </div>
                        <div className="passw-email">
                            <div className={validation.email.isInvalid && 'has-error'}>
                                <label>Email</label>
                                <div className="form-group">
                                    <input type="text" placeholder="johndoe@gmail.com" name="email" value={email}
                                           onChange={this.changeHandler}
                                           className="form-control input-height"/>
                                    <span className="help-block">{validation.email.message}</span>
                                </div>
                            </div>
                            <div className={validation.password.isInvalid && 'has-error'}>
                                <label>Password</label>
                                <div>
                                    <div className="form-group">
                                        <input type="password" placeholder="4 + caharacters" name="password"
                                               value={password} onChange={this.changeHandler}
                                               className="form-control input-height"/>
                                        <span className="help-block">{validation.password.message}</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="sign-up-w">
                            <button type="submit" onClick={this.submitHandler} className="btn-primary sing-up">SIGN UP
                            </button>
                        </div>
                        {
                            this.state.error && <div className="help-block">
                                User with such email already exist, please enter correct data
                            </div>
                        }
                        <div className="log-in-mobile">
                            <Link to="/login/" className="login-link-mobile">Already have an account?</Link>
                        </div>
                    </form>
                </div>
            </div>
        )
    }
}

export default Registration;
