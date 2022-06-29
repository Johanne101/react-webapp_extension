import React from "react";
import { render } from "react-dom";
import fetch from 'node-fetch';

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

render(<Popup />, document.getElementById("react-target"));
