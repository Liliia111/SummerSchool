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
            error : false
        };
    }

    changeHandler = event => {
        this.setState({[event.target.name]: event.target.value})
    };

    submitHandler = event => {
        event.preventDefault();

            axios
                .post('/api/v1/article/1/comments', {
                    'comment' : this.state.comment
                })
                .then(() => {
                    this.props.history.push('/home')
                })
                .catch(() => {
                     this.setState({error: true})
                })
    };

    render(){
        return(
            <div className="comment_block">
              <div >
                <form className="comment_input">
                    <img className="comment_img" src="/static/imgs/avatar.png" alt="ava" />
                    <input className="input_form" type="text" onChange={this.changeHandler} name="comment" placeholder="Write new comment"/>
                    <button type="submit" onClick={this.submitHandler} className="comment_button">Post comment</button>
                </form>
              </div>

            </div>
        )
    }

}

export default Comments;
