import React from "react";
import Header from "../Header";
import Sidebar from '../Sidebar'
import MostPopularBlock from '../MostPopularBlock'
import Footer from '../Footer'


class Home extends React.Component {
    render() {
        return <>
            <Header/>
            <Sidebar/>
            <MostPopularBlock/>
            <Footer/>
        </>
    }
}

export default Home;