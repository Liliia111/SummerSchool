import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './style.css';
import axios from '../../axios';


class Comments extends React.Component {

    constructor(props) {
        super(props);

          this.state = {
            articleId: 1,
            comment: '',
            commentsList: [],
            loggedUser: {},
            visible: true,
            error: false,
            logged: true,
            reversed: true,
            commentsLength: 2,
        };

        this.loginButton = (<button type="submit" onClick={this.submitLogging} className="comment_button">Log in</button>);
        this.postButton = (<button type="submit" onClick={this.submitHandler} className="comment_button">Post comment</button>);

        this.sortCommentsListNewest = this.sortCommentsListNewest.bind(this)
        this.sortCommentsListOldest = this.sortCommentsListOldest.bind(this)
        this.sortMostRecent = this.sortMostRecent.bind(this)
    }

    componentDidMount() {
      const{articleId} = this.state

      axios.get(`/api/v1/user/self/`)
        .then(res => {
          const loggedUser = res.data;
          this.setState({ loggedUser });
          console.log(articleId);
        })
        .catch(res => {
          this.setState({ logged: false });
        });


        axios.get(`/api/v1/articles/${articleId}/comments/`)
          .then(res => {
            const commentsList = res.data;
            this.setState({ commentsList: commentsList.reverse()});
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
    };

    submitHandler = event => {
        event.preventDefault();

            axios
                .post(`/api/v1/articles/${this.state.articleId}/comments/`, {
                    'comment' : this.state.comment
                })
                .then(() => {
                    const months_names = ['Jan', 'Fab', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
                    const day = new Date().getDate();
                    const month = new Date().getMonth();
                    var monthDate = `${months_names[month]} ${day}`;
                    const currentComments = [...this.state.commentsList];
                    currentComments.push({id: 'asdf', content: this.state.comment, date: monthDate, first_name: this.state.loggedUser.first_name, last_name: this.state.loggedUser.last_name})
                    this.setState({comment: '', commentsList: currentComments, commentsLength: currentComments.length} )
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
      return(
        <div> Posibly here can be some cont</div>
      )
    }

    sortMostRecent(event){
        const{commentsList} = this.state
        const{reversed} = this.state
        if(reversed){
            this.setState({
                commentsLength: 2
            })
        } else {
            let newCommentList = commentsList.reverse()

            this.setState({
                commentsList: newCommentList,
                reversed: true,
                commentsLength: 2
            })
        }
    }

    sortCommentsListNewest(event){
        const{commentsList} = this.state
        const{reversed} = this.state
        if (!reversed){
        let newCommentList = commentsList.reverse()

        this.setState({
            commentsList: newCommentList,
            reversed: true,
            commentsLength: commentsList.length
        })
        console.log(newCommentList);
        } else {
            this.setState({
                commentsLength: commentsList.length
            })
        }
    }

    sortCommentsListOldest(event){
        const{commentsList} = this.state
        const{reversed} = this.state
        if (reversed){
        let newCommentList = commentsList.reverse()

        this.setState({
            commentsList: newCommentList,
            reversed: false,
            commentsLength: commentsList.length
        })
        } else {
            this.setState({
                commentsLength: commentsList.length
            })
        }
    }


    monthDay(){
        var str = arguments[0]
        var month_num =  parseInt(str.slice(5, 7), 10) - 1
        var date_num = str.slice(8, 10)
        const months_names = ['Jan', 'Fab', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        var res = `${months_names[month_num]} ${date_num}`
        return (
            res
        )
    }

    getComments(){
        const items = []
        for(var i = 0; i < this.state.commentsLength; i++){
        items.push(<div>
        <div className="user-info">
                  <div className="img-width">
                    <img className="user-img" src="/static/imgs/avatar.png" alt="ava" />
                  </div>
                  <div className="user-name-date">
                    <div className="user-info-name">{this.state.commentsList[i].first_name} {this.state.commentsList[i].last_name}</div>
                    <div className="comment-date">{this.monthDay(this.state.commentsList[i].date)}</div>
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
        const logged = this.state.logged;
        const comment = this.state.comment;
        const comments = this.state.commentsList;

        return(
            <div className="comment_block">
              <div className="top_content">
                <div className="comm_num">
                  Comments({comments.length})
                </div>
                <div className="dropdown">
                  <p onClick={this.sortMostRecent} className="sorted">sotred by: Most recent</p>
                  <div className="dropdown-content">
                    <p onClick={this.sortCommentsListOldest}>Olders first</p>
                    <p onClick={this.sortCommentsListNewest}>Newest first</p>
                  </div>
                </div>
              </div>
              <div >
                <div className="comment_input">
                    <img className="comment_img" src="/static/imgs/avatar.png" alt="ava" />
                    <input className="input-form" type="text" onChange={this.changeHandler} onKeyPress={this.handleKeyPress} name="comment" placeholder="Write new comment" value={this.state.comment}/>
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
