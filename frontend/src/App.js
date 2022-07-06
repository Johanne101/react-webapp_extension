import fetch from 'node-fetch'
import React from 'react';
// import React { useState } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
  
    // Initializing the state 
    this.state = { 
      posts: [],
      postsText: "",
      thread_id:""
      // console.log(this.state.postsText)
    };
  }
  componentDidMount() {
    this.initthread();
  }

  sendRequest = async () => {
    console.log({
      "thread_id": this.state.thread_id, 
      "user_id":"0.0.0.0", 
      "post_content":this.state.postsText
    });
    await fetch('http://127.0.0.1:5000/api/v1/posts',
      {
        method: 'POST',
        headers: {"Content-Type": "application/json"}, 
        body: JSON.stringify({
          "thread_id": this.state.thread_id, 
          "user_id":"0.0.0.0", 
          "post_content":this.state.postsText
        })
      }
    );
    this.setState({posts: [
        ...this.state.posts,
        {post_content:this.state.postsText}
      ]
    })
  }
  
  handleChange = e => {
    this.setState({
      // ...state,
      [e.target.name]: e.target.value,
    })
  }

  async initthread() {
    let thread_id;
    let url = "err";

    chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
      url = tabs[0].url;
    });
    try {
      const res = await fetch('http://127.0.0.1:5000/api/v1/threads',
      {
        method: 'POST',
        headers: {"Content-Type": "application/json"}, 
        body: JSON.stringify({"url": url})
      });
      thread_id = await res.json();
      thread_id = thread_id.id;
    } catch(e){
      console.log(e);
    }
    if(!thread_id){
      const response = await fetch('http://127.0.0.1:5000/api/v1/thread_id/' + url); 
      thread_id = await response.text();
      thread_id = thread_id.slice(1,thread_id.length-2)  
    }
    const response_2 = await fetch(`http://127.0.0.1:5000/api/v1/threads/${thread_id}`)
    const thread = await response_2.json();
    const post_list = [];
    for(const el of thread.post_list) {
      const res = await fetch(`http://127.0.0.1:5000/api/v1/posts/${el}`)
      post_list.push(await res.json())
    }
    console.log('setting thread_id',thread_id)
    this.setState({ posts : post_list, thread_id })
  }
  
  create_posts() {
    return this.state.posts.map((element) =>  
      <div className="App-link">
        Post: {element.post_content}</div>  
    );  
  }
  render() {
    const posts = this.create_posts();
    console.log(this.state.postsText)
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>Spiel Ink</p>
            {posts}
          <div><button>Like</button><button>Dislike</button></div>
          <div>
            <body>
              <form>
                Post: <input name="postsText" type="text" onChange={this.handleChange} />
              </form>
              <button onClick={this.sendRequest}>Submit</button>
            </body>
          </div>
        </header>
      </div>
    );
  }
}
export default App;
