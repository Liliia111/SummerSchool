import React, { Component, PropTypes } from 'react';
import axios from '../../axios';
import removeMd from 'remove-markdown';
import 'bootstrap/dist/css/bootstrap.min.css';
import './style.css';
class Articles extends Component{
     constructor(props) {
        super(props);

        this.state = {
           article: []
        }
        this.getArticle = this.getArticle.bind(this)
    }
    componentDidMount() {
        this.getArticle();
    }


    getArticle = () => {
         console.log(this.props)
         axios
             .get(`/api/v1/articles/${this.props.match.params.id}/`)
             .then(res => {
                console.log(res);
                this.setState({ article : res.data });
            })
            .catch(err => {
                console.log(err);
            });
    }


   render(){
   const {article} = this.state
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
                         <p>Published /21.09.2019</p>
                         <h4>Article by Alex Kniupa / Assosiated Prass</h4>
                         <h2>{article.headline}</h2>
                     </div>
                <div className="shadow-box">
                </div>
                <div className="side-text">
                    <h1>NEWS</h1>
                </div>
                <div className="line-circle">
                    <hr></hr>
                    <h1>MORE ARTICLES</h1>
                </div>
                <div className="grid-box">
                    <div className="more-article-3">
                        <img src="/static/imgs/rectangle.svg" alt="BG"/>
                        <h1>Lorem ipsum</h1>
                        <p>Lorem ipsum dolor sit amet,  consectetur</p>
                    </div>
                    <div className="more-article-2">
                        <img src="/static/imgs/1.svg" alt="BG"/>
                        <h1>Lorem ipsum</h1>
                        <p>Lorem ipsum dolor sit amet,  consectetur</p>
                    </div>
                    <div className="more-article-1">
                        <img src="/static/imgs/2.svg" alt="BG"/>
                        <h1>Lorem ipsum</h1>
                        <p>Lorem ipsum dolor sit amet,  consectetur</p>
                    </div>
                </div>
                 <div className="grid-box-2">
                    <div className="more-article-4">
                        <img src="/static/imgs/rectangle.svg" alt="BG"/>
                        <h1>Lorem ipsum</h1>
                        <p>Lorem ipsum dolor sit amet,  consectetur</p>
                    </div>
                    <div className="more-article-5">
                        <img src="/static/imgs/1.svg" alt="BG"/>
                        <h1>Lorem ipsum</h1>
                        <p>Lorem ipsum dolor sit amet,  consectetur</p>
                    </div>
                    <div className="more-article-6">
                        <img src="/static/imgs/2.svg" alt="BG"/>
                        <h1>Lorem ipsum</h1>
                        <p>Lorem ipsum dolor sit amet,  consectetur</p>
                    </div>
                </div>

            </div>
   );
   }
}

export default Articles;