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
            <button className="navbar-toggler" type="button" data-toggle="collapse"
                    data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                    aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"/>
            </button>


            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <div className="search-icon">
                    <a href="#"> <img src="/static/imgs/search.png"/></a>
                </div>
                <div className="form-group has-search">
                    <div className="search-icon">
                        <input type="text" className="form-control" placeholder="Search"/>

                    </div>
                </div>
                <ul className="navbar-nav mr-auto">
                    <li className="nav-item active">
                        <div className="share-icon">
                            <a className="nav-link" href="#">Share <span className="sr-only">(current)</span></a>
                        </div>
                    </li>
                    <div className="icons">
                        <li className="nav-item">
                            <div className="facebook-icon-header">
                                <a href=""><img src="/static/imgs/fb.svg" alt="facebook"/></a>
                            </div>
                        </li>
                        <li className="nav-item">
                            <div className="google-icon-header">
                                <a href=""><img src="/static/imgs/gg.svg" alt="google"/></a>
                            </div>
                        </li>
                    </div>
                </ul>
                 <ul className="navbar-nav mr-auto">
                    <li className="nav-item">
                        <a className="nav-link" href="#" tabIndex="-1" aria-disabled="false">Log in</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#" tabIndex="-1" aria-disabled="false">Sign in</a>
                    </li>
                </ul>
                <ul className="navbar-nav mr-auto">
                    <li className="nav-item dropdown">
                        <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                           data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Language
                        </a>
                        <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                            <a className="dropdown-item" href="#">Action</a>
                            <a className="dropdown-item" href="#">Another action</a>
                            <div className="dropdown-divider"/>
                            <a className="dropdown-item" href="#">Something else here</a>
                        </div>
                    </li>
                </ul>
            </div>
        </nav>
    )
}

export default Header;