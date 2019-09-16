import React from 'react';
import { Link } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
//import '../styles/mainLogInFlow.css'
import './style.css';
import axios from '../../axios';


class Comments extends React.Component {

    constructor(props) {
        super(props);

          this.state = {
            comment: '',
            commentsList: [],
            loggedUser: {},
            visible: true,
            error: false,
            logged: true
        };

        this.loginButton = (<button type="submit" onClick={this.submitLogging} className="comment_button">Log in</button>)
        this.postButton = (<button type="submit" onClick={this.submitHandler} className="comment_button">Post comment</button>)
    }

    componentDidMount() {
      axios.get(`/api/v1/user/self/`)
        .then(res => {
          const loggedUser = res.data;
          this.setState({ loggedUser });
        })
        .catch(res => {
          this.setState({ logged: false });
        });


        axios.get(`/api/v1/articles/1/comments/`)
          .then(res => {
            const commentsList = res.data;
            this.setState({ commentsList });
          })
          .catch(res => {
            this.setState({ logged: false });
          });
    }

    changeHandler = event => {
        this.setState({[event.target.name]: event.target.value})
    };

    submitLogging = event => {
      this.props.history.push('/registration')
    }

    submitHandler = event => {
        event.preventDefault();

            axios
                .post("/api/v1/articles/1/comments/", {
                    'comment' : this.state.comment
                })
                .then(() => {
                    const currentComments = [...this.state.commentsList]
                    currentComments.push({id: 'asdf', content: this.state.comment, first_name: this.state.loggedUser.first_name, first_name: this.state.loggedUser.last})
                    this.setState({comment: '', commentsList: currentComments, } )
                    console.log(this.state.commentsList);
                })
                .catch(() => {
                     this.setState({error: true})
                })
    };

    handleKeyPress = (event) => {
      if (event.key == 'Enter') {
        this.setState({ visible: true })
      }
    };

    printSomeDiv(){
      console.log("Here we return some shit")
      return(
        <div> Posibly here can be some cont</div>
      )
    }

    sortCommentsList(){
        const myArray = this.state.commentsList

        myArray.sort((a, b) => a.item.date - b.item.date)
    }

    getComments(){
        const items = []
        for(var i = 0; i < this.state.commentsList  .length; i++){
        items.push(<div>
        <div className="user-info">
                  <div className="img-width">
                    <img className="user-img" src="/static/imgs/avatar.png" alt="ava" />
                  </div>
                  <div className="user-name-date">
                    <div className="user-info-name">{this.state.commentsList[i].first_name} {this.state.commentsList[i].last_name}</div>
                    <div className="comment-date">Mar 17</div>
                  </div>
                </div>
                <div className="comment-content">
                  {this.state.commentsList[i].content}
                </div>
        </div>
        )
        }
        return(
        items
        )
    }

    showButton(button){
      if(visible){
        return button
      } else {
        return button.style.display = "none"
      }
    };


    render(){
        const logged = this.state.logged
        const comment = this.state.comment
        const comments = this.state.commentsList

        return(
            <div className="comment_block">
              <div className="top_content">
                <div className="comm_num">
                  Comments({comments.length})
                </div>
                <div className="dropdown">
                  <span className="sorted">sotred by: Most recent</span>
                  <div className="dropdown-content">
                    <p>Olders first</p>
                    <p>Newest first</p>
                  </div>
                </div>
              </div>
              <div >
                <div className="comment_input">
                    <img className="comment_img" src="/static/imgs/avatar.png" alt="ava" />
                    <input className="input_form" type="text" onChange={this.changeHandler} onKeyPress={this.handleKeyPress} name="comment" placeholder="Write new comment" value={this.state.comment}/>
                    {logged ? (
                      this.postButton
                    ) : (
                      this.loginButton
                    )}
                </div>
              </div>
              {comments.length && <div className="comments">
                <div>{this.getComments()}</div>
              </div>}
            </div>
        )
    }

}

export default Comments;
