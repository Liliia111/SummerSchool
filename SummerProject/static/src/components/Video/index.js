import React, { Component, PropTypes } from 'react';
import axios from '../../axios';
import removeMd from 'remove-markdown';
import 'bootstrap/dist/css/bootstrap.min.css';
import './style.css';


class Video extends Component{
     constructor(props) {
        super(props);

        this.state = {
           article: [],
           articleList: []
        }
        this.getArticle = this.getArticle.bind(this)
        this.getArticleList = this.getArticleList.bind(this)
    }
    componentDidMount() {
        this.getArticle();
        this.getArticleList();
    }


    getArticle = () => {
         axios
             .get(`/api/v1/articles/${this.props.match.params.id}/`)
             .then(res => {
                this.setState({ article : res.data });
            });
         console.log(this.state.article);
    }
    getArticleList = () => {
          axios
             .get(`/api/v1/more_articles/`)
             .then(result => {
                this.setState({ articleList : result.data });
                console.log(this.state.articleList);
             });
    }

   render(){
   const {article} = this.state
   const {articleList} = this.state
   const data = articleList
   if(!article){
       return null;
   }
   return(
            <div className="video-view">
                <div className="vid-main">
                    <iframe width="814" height="544" src={article.video}>
                    </iframe>
                </div>
                <div className="side-text">
                    <h1>NEWS</h1>
                </div>
                <div className="lft-txt">
                    <h1>VIDEO</h1>
                </div>
                <div className="link-vid">
                    <a href="http://localhost:8000/videos/2/">
                    <img src="/static/imgs/1.svg" alt="EG"/>
                    </a>
                </div>
            </div>
   );
   }
}

export default Video;