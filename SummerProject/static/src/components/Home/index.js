import React from "react";
import Header from "../Header";
import Sidebar from '../Sidebar'
import MostPopularBlock from '../MostPopularBlock'
import Footer from '../Footer'
import PhotoOfTheDay from '../PhotoOfTheDay'


class Home extends React.Component {
    render() {
        return <>
            <Header/>
            <Sidebar/>
            <PhotoOfTheDay/>
            <MostPopularBlock/>
            <Footer/>
        </>
    }
}

export default Home;