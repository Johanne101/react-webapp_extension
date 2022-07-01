import React from "react";
import { render } from "react-dom";
import fetch from 'node-fetch';
const request = require('request');

function Popup() {


fetch('127.0.0.1:5000/api/v1/thread_id/testwebsite.com')
  .then(response => response.json("4c64310e-93ce-4f88-8be2-5311fb1aca4e"))
  .then(json => console.log(body))

fetch('127.0.0.1:5000/api/v1/threads/4c64310e-93ce-4f88-8be2-5311fb1aca4e')
	.then(response => console.log(body))
	.then(json => console.log(body))

	return (
		<div>
		<h1>Hello, world!</h1>
		<p>Active simple popup.</p>
		</div>
	);
}

// This will be in the restful api stored in memory and
// the api handlers will update this object
// - get all posts for site
// - create post
// - like post

const express = require('express')
const app = express()
const port = 5000


let posts = [{
  text: "here is some text",
  likes: 3
},{
  text: "here is some more text",
  likes: 0
}]

app.get('/api', (req, res) => {
  res.send(posts);
})

app.post('/', (req, res) => {
  res.send('Hello World Post!');
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

render(<Popup />, document.getElementById("react-target"));
