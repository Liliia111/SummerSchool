import React from 'react';
import {Link} from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/mainLogInFlow.css'
import './style.css';
import FormValidator from "../../validator/FormValidator";
import {rules} from "./validation_rules";
import axios from "../../axios";


class ResetPassword extends React.Component {

    constructor(props) {
        super(props);

        this.validator = new FormValidator(rules);

        this.state = {
            newPassword: '',
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
                .post('/api/v1/user/forgot_password_handler/', {
                    'new_password': this.state.newPassword,
                    'new_password_confirm': this.state.password,
                })
                .then(() => {
                    this.props.history.push('/login')
                })
                .catch(() => {
                    this.setState({error: true})
                })
        }
    };

    render() {
        const {newPassword, password} = this.state;
        let validation = this.submitted ?
            this.validator.validate(this.state) :
            this.state.validation;

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
                            <div className={validation.password.isInvalid && 'has-error'}>
                                <label>New password</label>
                                <div>
                                    <div className="form-group">
                                        <input type="password" placeholder="new password" name="newPassword"
                                               value={newPassword}
                                               onChange={this.changeHandler} className="form-control input-height"/>
                                    </div>
                                </div>
                            </div>
                            <div className={validation.password.isInvalid && 'has-error'}>
                                <label>Password</label>
                                <div>
                                    <div className="form-group">
                                        <input type="password" placeholder="confrim password" name="password"
                                               value={password}
                                               onChange={this.changeHandler} className="form-control input-height"/>
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
                                Passwords don't match. Please try again.
                            </div>
                        }
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
