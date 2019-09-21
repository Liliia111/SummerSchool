import React from 'react';
import {Tab, Tabs, TabList, TabPanel} from 'react-tabs';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/mainLogInFlow.css'
import './style.css';


class Registration extends React.Component {

    render() {

        return (
            <div>
                <div className="tab_place">
                    <ul className="nav justify-content-center row" role="tablist">
                        <li className="nav-item border col-sm-3">
                            <a className="nav-link bg-white text-dark" data-toggle="tab" href="#personal">Personal</a>
                        </li>
                        <li className="nav-item border col-sm-3">
                            <a className="nav-link bg-white text-dark" data-toggle="tab" href="http://localhost:8000/changePassword">Change
                                password</a>
                        </li>
                        <li className="nav-item border col-sm-3">
                            <a className="nav-link bg-white text-dark" data-toggle="tab" href="#my_surveys">My
                                surveys</a>
                        </li>
                        <li className="nav-item border col-sm-3">
                            <a className="nav-link bg-white text-dark" data-toggle="tab" href="#team_hub">Team hub</a>
                        </li>
                    </ul>
                </div>
            </div>
        )
    }
}


export default Registration;
