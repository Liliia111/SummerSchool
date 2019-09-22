import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/mainLogInFlow.css'
import './style.css';
import FormValidator from "../../validator/FormValidator";
import {rules} from "./validation_rules";
import axios from "../../axios";


class changePassword extends React.Component {

    constructor(props) {
        super(props);

        this.validator = new FormValidator(rules);

        this.state = {
            password: '',
            oldPassword: '',
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
                .put('/api/v1/user/change_password/', {
                    'old_password': this.state.oldPassword,
                    'new_password': this.state.password,
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
        const {password, oldPassword} = this.state;
        let validation = this.submitted ?
            this.validator.validate(this.state) :
            this.state.validation;

        return (
            <div className="change-password">
                <form className="form">
                    <div className="passw-email">
                        <div className={validation.password.isInvalid && 'has-error'}>
                            <label>Old password</label>
                            <div>
                                <div className="form-group">
                                    <input type="password" placeholder="old password" name="oldPassword"
                                           value={oldPassword}
                                           onChange={this.changeHandler} className="form-control input-height"/>
                                </div>
                            </div>
                        </div>
                        <div className={validation.password.isInvalid && 'has-error'}>
                            <label>New password</label>
                            <div>
                                <div className="form-group">
                                    <input type="password" placeholder="new password" name="password"
                                           value={password}
                                           onChange={this.changeHandler} className="form-control input-height"/>
                                    <span className="help-block">{validation.password.message}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="sign-up-w">
                        <button type="submit" onClick={this.submitHandler} className="btn-primary sing-up">CHANGE
                            PASSWORD
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

export default changePassword;
