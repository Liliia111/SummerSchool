import React from 'react';
import PropTypes from 'prop-types';
import './style3.css'
import axios from 'axios';

const drawerWidth = 253;


class PermanentDrawerLeft2 extends React.Component {
 state = {
    categories: []
  }

  componentDidMount() {
    axios.get("http://localhost:8000/api/v1/category/")
      .then(res => {
        const categories = res.data;
        this.setState({categories});
      })
  }

render(){
     const { classes } = this.props;
return (
<ul className="list" aria-haspopup="true">
 {this.state.categories.map((text) => (
     <li className="active">
         <a href="#" className="first-level" >{text}</a>
      </li>


  ))}

      </ul>

  );
}
  }



export default PermanentDrawerLeft2;