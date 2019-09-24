import React, { Component, PropTypes } from 'react';
import axios from '../../axios';
import removeMd from 'remove-markdown';
import 'bootstrap/dist/css/bootstrap.min.css';
import './style.css';

class Articles extends Component{
     constructor(props) {
        super(props);

        this.state = {
           article: [],
           articleList: [],
           articleArr: []
        }
        this.getArticle = this.getArticle.bind(this)
        this.getArticles = this.getArticles.bind(this)
        this.getArticles2 = this.getArticles2.bind(this)
    }

    componentDidMount() {
        this.getArticle();
        this.getArticles();
        this.getArticles2();
    }

    getArticle = () => {
         axios
             .get(`/api/v1/articles/${this.props.match.params.id}/`)
             .then(res => {
                this.setState({ article : res.data });
                console.log(this.state.article);

            });
    }

    getArticles = () => {
         axios
             .get(`/api/v1/more_articles/`)
             .then(result => {
                this.setState({ articleList : result.data });
                console.log(this.state.articleList);
             });
    }

     getArticles2 = () => {
         axios
             .get(`/api/v1/more_articles_2/`)
             .then(result => {
                this.setState({ articleArr : result.data });
                console.log(this.state.articleArr);
             });
    }

    render(){
    const {article} = this.state
    const {articleList} = this.state
    const {articleArr} = this.state
    const data = articleList;
    const data_2 = articleArr
    const listItems = data.map((d) =>
        <div key={d.id}>
                <div className="more-article-1">
                    <img src="/static/imgs/2.svg" alt="BG"/>
                    <h1>{d.category_id}</h1>
                    <p>{d.headline}</p>
                </div>
        </div>
        );
    const listItems_2 = data_2.map((d) =>
        <div key={d.id}>
            <div className="more-article-2">
                <img src="/static/imgs/1.svg" alt="BG"/>
                <h1>{d.category_id}</h1>
                <p>{d.headline}</p>
            </div>
        </div>
        );



    if(!article){
       return null;
       }
           return(
           <div className="article-view">
               <div className="imgBx">
                   <img src="/static/imgs/article-photo.svg" alt="BG"/>
               </div>
               <div className="text-article">
                   <p>{article.content}</p>
               </div>
               <div className="text-block">
                   <p>Published /{article.published_date}</p>
                   <h4>Article by {article.author}/ Assosiated Prass</h4>
                   <h2>{article.headline}</h2>
               </div>
               <div className="shadow-box"></div>
               <div className="side-text">
                   <h1>NEWS</h1>
               </div>
               <div className="left-txt">
                   <h1>{article.category}</h1>
               </div>
               <div className="mor-art">
                   <div className="line-circle">
                       <hr></hr>
                       <h1>MORE ARTICLES</h1>
                   </div>
                   <div className="grid-box">
                       {listItems}
                       </div>
                   </div>
                   <div className="grid-box-2">
                       {listItems_2}
                   </div>
           </div>


           );
           }
           }

export default  Articles;
