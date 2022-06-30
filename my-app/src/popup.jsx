import React from "react";
import { render } from "react-dom";
import fetch from 'node-fetch';
const request = require('request');

function Popup() {

const response = await fetch('localhost:3000');
const body = await response.text();

console.log(body);
    return (
        <div>
            <h1>Hello, world!</h1>
            <p>Active simple popup.</p>
        </div>
    );
}
let posts = [{
  text: "here is some text"
  likes: 3
},{
  text: "here is some more text"
  likes: 0
}]

This will be in the restful api stored in memory and the api handlers will update this object
- get all posts for site
- create post
- like post
const express = require('express')
const app = express()
const port = 8080
let posts = [{
  text: "here is some text"
  likes: 3
},{
  text: "here is some more text"
  likes: 0
}]

app.get('/api, (req, res) => {
  res.send(posts);
})

app.post('/', (req, res) => {
  res.send('Hello World Post!')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

render(<Popup />, document.getElementById("react-target"));
