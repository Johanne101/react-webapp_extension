import React from "react"; 7.2K (gzipped: 2.9K)
import { render } from "react-dom"; 119.8K (gzipped: 39K)

function Popup() {
    return (
        <div>
            <h1>Hello, world!</h1>
            <p>Active simple popup.</p>
        </div>
    );
}

render(<Popup />, document.getElementById("react-target"));
