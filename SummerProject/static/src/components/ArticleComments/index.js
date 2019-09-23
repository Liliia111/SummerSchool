import React from "react";
import Header from "../Header";
import Sidebar from '../Sidebar'
import Articles from '../Articles'
import Comments from '../Comments'
import Footer from '../Footer'


class ArticleComments extends React.Component {
    render() {
        return <>
            <Header/>
            <Sidebar/>
            <Articles/>
        </>
    }
}

export default ArticleComments;