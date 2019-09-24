import React from "react";
import PropTypes from "prop-types";
import axios from '../../axios';
import "./style.css";

class Header extends React.Component{
  state = {
    loggedUser: {},
    logged: true
  };

  componentDidMount() {
        axios.get(`/api/v1/user/self/`)
        .then(res => {
          const loggedUser = res.data;
          this.setState({ loggedUser });
          console.log(articleId);
        })
        .catch(res => {
          this.setState({ logged: false });
        });
  }

    render() {
    return (
       <nav className="navbar navbar-expand-lg navbar-light">
        <a className="navbar-brand" href="#">
          <div className="logotype">
            Sport News
          </div>
        </a>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon">
          </span></button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <div className="search-icon">
            <a href="#"> <img src="http://www.endlessicons.com/wp-content/uploads/2012/12/search-icon.png" /></a>
          </div>
          <div className="form-group has-search">
            <div className="search-icon">
              <input type="text" className="form-control" placeholder="Search by" />
            </div>
          </div>
          <div className="vl" style={{marginLeft: '500px'}} />
          <ul className="navbar-nav mr-auto">
            <li className="nav-item active">
              <div className="share-icon">
                <a className="nav-link" href="#">Share <span className="sr-only">(current)</span></a>
              </div>
            </li>
            <div className="icons">
              <li className="nav-item">
                <a href><img className="facebook-icon" src="http://endlessicons.com/wp-content/uploads/2012/10/facebook-icon-614x460.png" alt="facebook" /></a>
              </li>
              <li className="nav-item">
                <a href><img className="google-icon" src="http://endlessicons.com/wp-content/uploads/2012/10/google-plus-icon-614x460.png" alt="google" /></a>
              </li>
              <li className="nav-item">
                <a href><img className="twitter-icon" src="http://endlessicons.com/wp-content/uploads/2012/10/twitter-icon-614x460.png" /></a>
              </li>
            </div>
            <div className="vl" style={{marginLeft: '70px'}} />
          </ul>

          {this.state.logged == true && ( <ul className="navbar-nav mr-auto">
          <li className="nav-item">
          <span className="user-pic" />
        </li>
        <li className="nav-item">
          <a className="nav-link name-surname" href="#" tabIndex={-1} aria-disabled="false">Ivan Baloh</a>
        </li>
        <li className="nav-item">

          <span className="down-arrow" href="#" tabIndex={-1} aria-disabled="false">
            <span className="tooltiptext"><span className="nameintools">Ivan Baloh</span><br />
              <span className="subtoolemail">ivanbaloh@gmail.com</span>
              <div className="view-profile-btn">VIEW PROFILE</div>
            <span className="log-o1">Personal</span>
            <span className="log-o">Change password</span>
            <span className="log-o">Log out</span>
            </span>


          </span>
        </li>
         </ul>
        )}

        {this.state.logged == false && (<ul className="navbar-nav mr-auto"><li className="nav-item">
              <a className="nav-link sign-up-header" href="http://localhost:8000/registration/" tabIndex={-1} aria-disabled="false">Sign up</a>
            </li>
            <li className="nav-item">
              <div className="sign-in-sec2">
                <a className="nav-link log-in-header" href="http://localhost:8000/login" tabIndex={-1} aria-disabled="false">Log in</a>
            </div>
            </li> </ul>)}

          <ul className="navbar-nav mr-auto">
            <li className="nav-item dropdown">
              <a className="nav-link dropdown-toggle leng" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                EN
              </a>
              <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                <a className="dropdown-item" href="#">Action</a>
                <a className="dropdown-item" href="#">Another action</a>
                <div className="dropdown-divider">
                  <a className="dropdown-item" href="#">Something else here</a>
                </div>
              </div></li>
          </ul>
        </div>
      </nav>
    );
}
}

export default Header;

