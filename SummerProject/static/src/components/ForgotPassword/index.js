import React from 'react';
import {Link} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/mainLogInFlow.css';
import '../LogIn/style.css';
import './style.css';
import FormValidator from "../../validator/FormValidator";
import {rules} from "./validation_rules";
import axios from "../../axios";


class ForgotPassword extends React.Component {
    constructor(props) {
        super(props);

        this.validator = new FormValidator(rules);

        this.state = {
            email: '',
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
                .post('/api/v1/user/forgot_password/', {
                    'email': this.state.email,
                })
                .then(() => {
                    this.props.history.push('/check-email', this.state)
                })
                .catch(() => {
                     this.setState({error: true})
                })
        }
    };

    render() {
        const {email} = this.state;
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
                    <Link to="/registration/" className="btn btn-primary login login-link">Get Started</Link>
                </div>
                <div className="backgr-photo bg">
                    <img src="/static/imgs/login.jpg" alt="BG"/>
                </div>

                <div className="main background">
                    <h1>Forgot your password?</h1>
                    <form className="form">
                        <h3>Enter your email address below and we'll get you back on track</h3>
                        <div className="passw-email">
                            <div className={validation.email.isInvalid && 'has-error'}>
                                <label>Email address</label>
                                <div className="form-group">
                                    <input type="text" placeholder="johndoe@gmail.com" name="email" value={email}
                                           onChange={this.changeHandler} className="form-control input-height"/>
                                    <span className="help-block">{validation.email.message}</span>
                                </div>
                            </div>
                        </div>
                        <div className="sign-up-w">
                            <button type="submit" onClick={this.submitHandler} className="btn-primary sing-up">REQUEST
                                RESENT LINK
                            </button>
                        </div>
                        {
                            this.state.error && <div className="help-block">
                                User with such email doesn't exist, please enter correct data
                            </div>
                        }
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
