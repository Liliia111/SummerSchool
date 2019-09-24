import React from "react";
import PropTypes from "prop-types";
import "bootstrap/dist/css/bootstrap.min.css";
import axios from '../../axios';
import "./style.css";

class PhotoOfTheDay extends React.Component {
    state = {
        popular: [],
        error: false
    };

    componentDidMount() {
        axios.get("/api/v1/articles/most_popular/")
            .then(res => {
                const popular = res.data[0];
                this.setState({popular});
            })
            .catch(res => {
                this.setState({error: true});
            });
    }

    render() {
        return (
            <div className="photo-of-the-day">
                <div className="container-fluid">
                    <div className="photo-of-the-day-block ">
                        <span className="divider-photo"/>
                        <div className="photo-container">
                            <p>PHOTO OF THE DAY</p>
                        </div>
                        <span className="divider-photo"/>
                    </div>
                </div>
                <div className="container-fluid">
                    <div className="triangle-right">
                        <p>
                            photo <span style={{fontWeight: "normal"}}>of the</span> day
                        </p>
                    </div>
                    <div className="item">
                        <img src="/static/imgs/index.jpeg" className="img-fluid" alt="Responsive image"/>
                        <div className="gradient"/>
                        <div className="carousel-caption">
                            <h3>{this.state.popular.headline}</h3>
                            <p>Los Angeles Lakes guard Derek Fisher, right, is pressured by the Denver Nuggets Nene during th efirst quarter of NBA exhibition action on Oct 16</p>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default PhotoOfTheDay;
