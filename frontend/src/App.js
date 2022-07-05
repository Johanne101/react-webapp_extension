import fetch from 'node-fetch'
import React from 'react';
// import { Component } from 'react';
import logo from './logo.svg';
import './App.css';

  class App extends React.Component {
  constructor(props) {
    super(props);
  
    // Initializing the state 
    this.state = { 
      posts: [
          {
            "user_id": "", 
            "post_content": "testing content", 
            "thread_id": "", 
            "id": "6ba5e073-dece-463c-9959-99053d714e3f", 
            "created_at": "2022-06-24T19:14:23.284395", 
            "updated_at": "2022-06-24T19:14:23.284498", 
            "__class__": "Post"
          },
          {
            "user_id": "", 
            "post_content": "testing content2", 
            "thread_id": "", 
            "id": "6ba5e073-dece-463c-9959-99053d714e3f", 
            "created_at": "2022-06-24T19:14:23.284395", 
            "updated_at": "2022-06-24T19:14:23.284498", 
            "__class__": "Post"
          }
      ],
    };
  }
  componentDidMount() { 
    // const response = fetch('127.0.0.1:5000/api/v1/posts');
    // const data = response.json();
    
    // this.setState({ posts : data })
  }
  create_posts() {
    return this.state.posts.map((element) =>  
      <div className="App-link">
        Post: {element.post_content}</div>  
    );  
  }
  render() {
    const posts = this.create_posts();
    return (
      <div className="App">
        
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload</p>
            {/* <div className="App-link">Post:post1</div>  
            <div className="App-link">Post:post2</div>*/}
            {posts}
          <div><button>Like</button><button>Dislike</button></div>
          <div>
            <body>
              <form>
                Post: <input type=""></input>
              </form>
            </body>
          </div>
        </header>
      </div>
    );
  }
}
export default App;
