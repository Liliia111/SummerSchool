import React from 'react';
import '../styles/mainLogInFlow.css'
import './style.css';
import axios from '../../axios';
import FormValidator from "../../validator/FormValidator";
import {rules} from "../ResetPassword/validation_rules";
import {Link} from "react-router-dom";


class ChangePassword extends React.Component {
    constructor(props) {
        super(props);

        this.validator = new FormValidator(rules);

        this.state = {
            newPassword: '',
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

    };

    render() {
        const {newPassword, oldPassword} = this.state;
        let validation = this.submitted ?
            this.validator.validate(this.state) :
            this.state.validation;
        return (
            <div>
                <div id="change_password" className="container tab-pane "><br/>
                    <div className="lol">
                        <form>
                            <div className={validation.password.isInvalid && 'has-error'}>
                                <label className="text_password">Old password</label>
                                <input type="password" name="oldPassword" placeholder={"old password"} value={oldPassword}
                                       onChange={this.changeHandler}/>
                            </div>
                            <div className={validation.password.isInvalid && 'has-error'}>
                                <label className="text_password">New password</label>
                                <input type="password" name="newPassword" placeholder={"new password"} value={newPassword}
                                       onChange={this.changeHandler}/>
                                <span className="help-block">{validation.password.message}</span>
                            </div>

                            <div className="sign-up-new">
                                <button type="submit" onClick={this.submitHandler}
                                        className="btn-primary sing-up">CHANGE PASSWORD
                                </button>
                            </div>
                            {
                                this.state.error && <div className="help-block">
                                    Passwords don't match. Please try again.
                                </div>
                            }
                        </form>
                    </div>
                </div>
            </div>
        )
    }
}

export default ChangePassword;
