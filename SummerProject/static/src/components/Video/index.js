import React, { Component, PropTypes } from 'react';
import axios from '../../axios';
import removeMd from 'remove-markdown';
import 'bootstrap/dist/css/bootstrap.min.css';
import './style.css';


class Video extends Component{
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
         axios
             .get(`/api/v1/articles/${this.props.match.params.id}/`)
             .then(res => {
                this.setState({ article : res.data });
            });
         console.log(this.state.article);
    }


   render(){
   const {article} = this.state
   if(!article){
       return null;
   }
   return(
            <div className="article-view">
                <div className="vid-main">
                    <iframe width="814" height="544" src={article.video}>
                    </iframe>
                </div>
                <div className="side-text">
                    <h1>NEWS</h1>
                </div>
                <div className="left-txt">
                    <h1>VIDEO</h1>
                </div>

            </div>
   );
   }
}

export default Video;