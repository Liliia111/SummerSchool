import React from "react";
import PropTypes from "prop-types";
import "bootstrap/dist/css/bootstrap.min.css";
import axios from "axios";
import "./style.css";

const instance = axios.create({
    baseURL: 'http://localhost:8000'
});


class MostPopularBlock extends React.Component {
  state = {
    popularList: [],
    commentedList: [],
    error: false
  };

  componentDidMount() {
    axios.all([
        axios.get("/api/v1/articles/most_popular/"),
        axios.get("/api/v1/articles/most_commented/")
      ])
      .then(
        axios.spread((viewsRes, commentRes) => {
          const popularList = viewsRes.data;
          const commentedList = commentRes.data;
          this.setState({ popularList });
          this.setState({ commentedList });
        })
      )
      .catch(
        axios.spread((viewsRes, commentRes) => {
          this.setState({ error: true });
        })
      );
  }

  render() {
    return (
      <div class="most-section">
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
                      <img className src="/static/imgs/sport1.png" alt={popularArticle.headline}
                      />
                    </div>
                    <div className="card-body">
                      <h4 className="card-title" key={popularArticle.id}>
                        {popularArticle.headline}
                      </h4>
                      <p className="card-text">{popularArticle.content}</p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
            <div class="col-md-auto">
              <div class="most-comments">
                MOST COMMENTS
                <div class="divider-comments"></div>
              </div>
              {this.state.commentedList.map(commentedArticle => (
                <div className="card">
                  <div className="card-horizontal">
                    <div className="img-square-wrapper">
                      <img className src="/static/imgs/sport1.png" alt={commentedArticle.headline}/>
                    </div>
                    <div className="card-body">
                      <h4 className="card-title" key={commentedArticle.id}>
                        {commentedArticle.headline}
                      </h4>
                      <p className="card-text">{commentedArticle.content}</p>
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
