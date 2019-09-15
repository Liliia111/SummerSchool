import React from "react";
import Header from "../Header";
import Sidebar from '../Sidebar'
import Footer from '../Footer'


class Home extends React.Component {
    render() {
        return <>
            <Header/>
           <Sidebar/>
           <Footer/>
        </>
    }
}

export default Home;