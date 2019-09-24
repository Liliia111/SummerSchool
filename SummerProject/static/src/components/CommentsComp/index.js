import React from "react";
import Header from "../Header";
import Comments from '../Comments'
import Footer from '../Footer'


class CommentsComp extends React.Component {
    render() {
        return <>
            <Header/>
            <Comments/>
            <Footer/>
        </>
    }
}

export default CommentsComp;