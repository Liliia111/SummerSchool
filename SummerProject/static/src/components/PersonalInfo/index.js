import React from 'react';
import {Tab, Tabs, TabList, TabPanel} from 'react-tabs';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/mainLogInFlow.css'
import './style.css';
import Header from "../Header";
import Sidebar from '../Sidebar'
import {
    Route,
    NavLink,
    BrowserRouter as Router,
} from 'react-router-dom';
import ChangePassword from '../ChangePassword'


class PersonalInfo extends React.Component {

    render() {

        return <>
            <Header/>
            <Sidebar/>
            <div>
                <Router>
                    <div className="tab_place">
                        <ul className="nav justify-content-center row" role="tablist">
                            <li className="nav-item border col-sm-3">
                                <a className="nav-link bg-white text-dark" data-toggle="tab"
                                   href="#personal">Personal</a>
                            </li>
                            <li className="nav-item border col-sm-3">
                                <NavLink
                                    className='button change-pasword-nav'
                                    exact activeClassName='active'
                                    to='/changePassword'
                                >
                                    Change Password
                                </NavLink>
                            </li>
                            <li className="nav-item border col-sm-3">
                                <a className="nav-link bg-white text-dark" data-toggle="tab" href="#my_surveys">My
                                    surveys</a>
                            </li>
                            <li className="nav-item border col-sm-3">
                                <a className="nav-link bg-white text-dark" data-toggle="tab" href="#team_hub">Team
                                    hub</a>
                            </li>
                        </ul>
                        <Route
                            exact path='/changePassword'
                            component={ChangePassword}
                        />
                    </div>
                </Router>
            </div>
        </>
    }
}


export default PersonalInfo;