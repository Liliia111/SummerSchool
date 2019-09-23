import React from 'react';
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
import userData from "../UserData";
import axios from "../../axios";


class PersonalInfo extends React.Component {

    componentDidMount() {
        axios.get(`/api/v1/user/self/`)
            .then(res => {
                const loggedUser = res.data;
                this.setState({loggedUser});
            })
            .catch(res => {
                this.props.history.push('/login')
            });
    }



    render() {

        return <>
            <Header/>
            <Sidebar/>
            <div>
                <Router>
                    <div className="tab_place">
                        <ul className="nav justify-content-center row" role="tablist">
                            <li className="nav-item border col-sm-3">
                                <NavLink
                                    className='button change-pasword-nav'
                                    exact activeClassName='active'
                                    to='/userData'
                                >
                                    Personal
                                </NavLink>
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
                            exact path='/userData'
                            component={userData}
                        />
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