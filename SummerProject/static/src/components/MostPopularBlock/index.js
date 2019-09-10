import React from "react";
import PropTypes from "prop-types";
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from '../../axios';
import "./style.css";

class MostPopularBlock extends React.Component {
  state = {
    popularList: [],
    error: false
  };

  componentDidMount() {
    axios.get("/api/v1/articles/most_popular/")
      .then(res => {
        const popularList = res.data;
        this.setState({ popularList });
      })
      .catch(res => {
        this.setState({ error: true });
      });
  }

  render() {
    return (
    <div class ="most-section">
    <div className="container-fluid">
        <div className="row">
          <div className="col-md-auto">
            <div className="most-popular">
              MOST POPULAR
              <div className="divider-popular" />
            </div>
            {this.state.popularList.map(popularArticle => (
            <div className="card">
              <div className="card-horizontal">
                <div className="img-square-wrapper">
                  <img className src="sport1.png" alt={popularArticle.headline} />
                </div>
                <div className="card-body">
                  <h4 className="card-title" key={popularArticle.id}>{popularArticle.headline}</h4>
                  <p className="card-text">{popularArticle.content}</p>
                </div>
              </div>
            </div>
            ))}
          </div>
        </div>
      </div>
    </div>
    );
  }
}

export default MostPopularBlock;
