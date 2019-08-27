import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/mainLogInFlow.css'
import './style.css';
import axios from 'axios';
import FormValidator from './FormValidator';



const API_URL = 'http://localhost:8000';


class Registration extends React.Component {
    constructor(props) {
        super(props);

        this.validator = new FormValidator([
          {
            field: 'first_name',
            method: 'isEmpty',
            validWhen: false,
            message: 'First name is required!',
          },
          {
            field: 'first_name',
            method: 'isLength',
            args: [ { max:50 } ],
            validWhen: true,
            message: 'First name can contain less than 50 char!',
          },
          {
            field: 'last_name',
            method: 'isEmpty',
            validWhen: false,
            message: 'Last name is required!',
          },
          {
            field: 'last_name',
            method: 'isLength',
            args: [ { max:50 } ],
            validWhen: true,
            message: 'Last name can contain less than 50 char!',
          },
          {
            field: 'email',
            method: 'isEmpty',
            validWhen: false,
            message: 'Email is required!',
          },
          {
            field: 'email',
            method: 'isEmail',
            validWhen: true,
            message: 'That is not a valid email!',
          },
          {
            field: 'password',
            method: 'isEmpty',
            validWhen: false,
            message: 'Password is required!',
          },
          {
            field: 'password',
            method: 'isLength',
            args: [ { min:4, max:255 } ],
            validWhen: true,
            message: 'Password must contain more than 4 character and less than 255!',
          },
        ]);

        this.state = {
            first_name: '',
            last_name: '',
            email: '',
            password: '',
            validation: this.validator.valid(),
            redirectToReferrer: false,
            error : false
        };
    }

    changeHandler = event => {
        this.setState({[event.target.name]: event.target.value})
    };

    submitHandler = event => {
        event.preventDefault();
        console.log(this.state);
        const validation = this.validator.validate(this.state);
        this.setState({validation});
        this.submitted = true;

        if (validation.isValid) {
            axios
                .post(API_URL + '/api/v1/user/registration/', {
                    'first_name': this.state.first_name,
                    'last_name': this.state.last_name,
                    'email': this.state.email,
                    'password': this.state.password,
                })
                .then(() => {
                    this.props.history.push('/home')
                })
                .catch(() => {
                     this.setState({error: true})
                })
        }
    };


    render() {
        const {first_name, last_name, email, password} = this.state;
        let validation = this.submitted ?
                      this.validator.validate(this.state) :
                      this.state.validation;

        return (
            <div className="login-page">
                <div className="logo">
                    <a href="http://localhost:8000/home/">Sport News</a>
                </div>
                <div className="log-in">
                    <a href="http://localhost:8000/login/">Already have an account?</a>
                    <a href="http://localhost:8000/login/" className="btn btn-primary login">Log In</a>
                </div>
                <div className="left-part bg">
                    <img src="/static/imgs/login.jpg" alt="BG"/>
                </div>

                <div className="right-part background">
                    <h1>Create Account</h1>
                    <div>
                        <a href="#" className="fb">
                            <img className="icon-style"/>
                        </a>

                        <a href="#" className="gg">
                            <img className="icon-style"/>
                        </a>
                    </div>
                    <p>Or use your email for registration:</p>
                    <form onSubmit={this.submitHandler} className="form">
                        <div className="user-data">
                            <div className="form-group">
                                <div className={validation.first_name.isInvalid && 'has-error'}>
                                    <label>First Name</label>
                                    <input type="text" placeholder="John" name="first_name" value={first_name}
                                           onChange={this.changeHandler} className="form-control"/>
                                    <span className="help-block">{validation.first_name.message}</span>
                                </div>
                            </div>
                            <div className="form-group ">
                                <div className={validation.last_name.isInvalid && 'has-error'}>
                                    <label>Last Name</label>
                                    <input type="text" placeholder="Doe" name="last_name" value={last_name}
                                           onChange={this.changeHandler} className="form-control"/>
                                    <span className="help-block">{validation.last_name.message}</span>
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
                            <a href="http://localhost:8000/login/">Already have an account?</a>
                        </div>
                    </form>
                </div>
            </div>
        )
    }
}

export default Registration;
