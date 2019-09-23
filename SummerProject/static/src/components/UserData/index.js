import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/mainLogInFlow.css'
import './style.css';
import FormValidator from "../../validator/FormValidator";
import {rules} from "./validation_rules";
import axios from "../../axios";


class userData extends React.Component {

    constructor(props) {
        super(props);

        this.validator = new FormValidator(rules);

        this.state = {
            oldPassword: '',
            password: '',
            firstName: '',
            lastName: '',
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
                .put('/api/v1/user/self/', {
                    'first_name': this.state.firstName,
                    'last_name': this.state.lastName,
                    'email': this.state.email
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
        const {firstName, lastName, email} = this.state;
        let validation = this.submitted ?
            this.validator.validate(this.state) :
            this.state.validation;

        return (
            <div className="change-password">
                <form className="form">
                    <div className="passw-email">
                        <div className={validation.firstName.isInvalid && 'has-error'}>
                            <label>First name</label>
                            <div>
                                <div className="form-group">
                                    <input type="text" placeholder="John" name="firstName" value={firstName}
                                           onChange={this.changeHandler} className="form-control input-height"/>
                                    <span className="help-block">{validation.firstName.message}</span>
                                </div>
                            </div>
                        </div>
                        <div className={validation.lastName.isInvalid && 'has-error'}>
                            <label>Last name</label>
                            <div>
                                <div className="form-group">
                                    <input type="text" placeholder="Doe" name="lastName" value={lastName}
                                           onChange={this.changeHandler} className="form-control input-height"/>
                                    <span className="help-block">{validation.lastName.message}</span>
                                </div>
                            </div>
                        </div>
                        <div className={validation.email.isInvalid && 'has-error'}>
                            <label>Email</label>
                            <div>
                                <div className="form-group">
                                    <input type="text" placeholder="johndoe@gmail.com" name="email" value={email}
                                           onChange={this.changeHandler}
                                           className="form-control input-height"/>
                                    <span className="help-block">{validation.email.message}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <button type="submit" onClick={this.submitHandler}
                                className="btn-primary change-password-submit">UPDATE PROFILE
                        </button>
                    </div>
                    {
                        this.state.error && <div className="help-block">
                            Please try later, now this function is disabled!
                        </div>
                    }
                </form>
            </div>
        )
    }
}

export default userData;
