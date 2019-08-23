import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles, withStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import CssBaseline from '@material-ui/core/CssBaseline';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import InboxIcon from '@material-ui/icons/MoveToInbox';
import MailIcon from '@material-ui/icons/Mail';
import axios from 'axios';
import { createMuiTheme } from '@material-ui/core/styles';
import { sizing } from '@material-ui/system';
const drawerWidth = 253;
import './style3.css'

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
         <a href="#homeSubmenu" className="first-level" >{text}</a>
      </li>


  ))}

      </ul>

  );
}
  }



export default PermanentDrawerLeft2;