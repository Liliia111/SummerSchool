import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './style.css';

class Footer extends React.Component {
    render() {
        return (
            <div className="Footer">
                <footer className="section footer-classic context-dark bg-image">
                    <div className="container">
                        <div className="row row-30">
                            <div className="col-md-4 col-xl-3">
                                <div>
                                    <h5 className="title">COMPANY INFO</h5>
                                </div>
                                <ul className="nav-list">
                                    <li><a href="#">About Sport News</a></li>
                                    <li><a href="#">News/In the Press</a></li>
                                    <li><a href="#">Advertising</a></li>
                                    <li><a href="#">Events</a></li>
                                    <li><a href="#">Contact Us</a></li>
                                </ul>
                            </div>
                            <div className="col-md-4">
                                <div>
                                    <h5 className="title">CONTRIBUTORS</h5>
                                </div>
                                <ul className="nav-list">
                                    <li><a href="#">Featured Writers Program</a></li>
                                    <li><a href="#">Featured Team Writers Program</a></li>
                                    <li><a href="#">Internship Program</a></li>
                                </ul>
                            </div>
                            <div className="col-md-4 col-xl-3">
                                <div>
                                    <h5 className="title">NEWSLETTER</h5>
                                </div>
                                <ul className="nav-list">
                                    <li><a href="#">Sign up to recieve the latest in sport news</a></li>
                                    <form className="example" action="/action_page.php">
                                        <div className="subscribe">
                                            <input type="text" placeholder="Your email address" name="search2"/>
                                            <input type="submit" value="Subscribe"/>
                                        </div>
                                    </form>
                                    <li>
                                        <div className="icons">
                                            <div className="Sign-up">Sign up by</div>
                                            <div className="facebook-icon">
                                                <img src="/static/src/components/Footer/imgs/fb.svg" alt="facebook"/>
                                            </div>
                                            <div className="google-icon">
                                                <img src="/static/src/components/Footer/imgs/gg.svg" alt="google"/>
                                            </div>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div className="row no-gutters social-container">
                        <div className="col-md-6">
                            <a className="social-inner-left" href="#">
                                <h6>
                                    <span>
                                        <div className="sport-news-logo"> Sport News </div>
                                    </span>
                                </h6>
                            </a>
                        </div>

                        <div className="col-md-6">
                            <a className="social-inner-right">
                                <h6><span>
                                    <div className="copyright">
                                        Copyright © 2019 Sport News
                                        <br/>
                                        Privacy/Terms</div>
                                </span></h6>
                            </a>
                        </div>
                    </div>
                </footer>
            </div>
        )
    }
}

export default Footer;
