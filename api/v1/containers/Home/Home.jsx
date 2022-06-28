import React, { Component } from 'react';
import classes from './Home.module.css';

class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {
        }
    }

    // place to fetch things when the page loads
    componentDidMount() {
        
    }
  
    render() {
        return (        
            <div>
                <h1>Hello, world!</h1>
                <p>Active simple popup.</p>
            </div>
        );
    }
  }
  
  export default Home;
