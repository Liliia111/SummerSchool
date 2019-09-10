import React from "react";
import Footer from '../Footer'
import Sidebar from '../Sidebar'
import MostPopularBlock from '../MostPopularBlock'

class Home extends React.Component {
    render() {
        return <>
            <Sidebar/>
            <MostPopularBlock/>
            <Footer/>
        </>
    }
}

export default Home;