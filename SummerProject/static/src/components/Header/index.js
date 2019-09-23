import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './style.css';

function Header() {
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
          <ul className="navbar-nav mr-auto">
            <li className="nav-item">
              <a className="nav-link sign-up-header" href="http://localhost:8000/registration/" tabIndex={-1} aria-disabled="false">Sign up</a>
            </li>
            <li className="nav-item">
              <div className="sign-in-sec2">
                <a className="nav-link log-in-header" href="http://localhost:8000/login" tabIndex={-1} aria-disabled="false">Log in</a>
            </div>
            </li>
          </ul>
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
    )
}

export default Header;

