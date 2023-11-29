```html
<!DOCTYPE html>
<html>
    <head>
        <title>Searching System</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" href="assets/css/main.css" />
		<script src="assets/js/jQuery.js"></script>
        <script src="assets/js/main.js"></script>
    </head>
    <body class="wrap">
        <section class="banner">
            <div id="box">
                <div id="content">
                    <div id="text">Article Outline Extractor</div>    
                </div>
            </div>
            <div id="textio">
                <textarea id="inputText" placeholder="Please enter your article here......"></textarea>
                <textarea id="inputText" placeholder="Please enter your article here......"></textarea>
                <textarea id="inputText" placeholder="Please enter your article here......"></textarea>
            </div>
            <div id="button">
                <button id="extract" onclick="extractOutline()"">Extract Outline</button>
            </div>
        </section>
        <script src="assets/js/main.js"></script>
    </body>
</html>
```

```css
@charset "utf-8";

html {
    background: #1c1d26;
    height: 100%;
    margin: 0;
}

body {
    color: rgba(255, 255, 255, 0.75);
	font-family: "Roboto", Helvetica, sans-serif;
	font-size: 1.25em;
	font-weight: 100;
	line-height: 1.75em;
    align-items: center;
}

.wrap {
    min-height: 100%;
    margin-bottom: -10%;
}

.banner {
    background-color: rgba(0, 0, 0, .6);
    background-blend-mode: multiply;
	background-image: url("../../images/main.jpg");
    background-size: cover;
    background-attachment: fixed;
    background-position: center center;
    background-repeat: no-repeat;
    min-height: 100vh;
    width: 100%;
    border: 0em;
    margin: 0%;
    align-items: center;
    justify-content: center;
}

.banner #box {
    display: flex;
    align-items: center;
    justify-content: center;
}

.banner #box #content {
    margin-top: 5em;
}

@media screen and (max-width: 768px) {
    body {
        overflow-x: hidden;
    }
    .banner #box #content {
        margin-top: 8em;
        font-size: 0.8em;
    }
    ul {
        margin-right: -1em;
    }
    textarea {
        width: 20em;
        height: 30em;
        margin: 0.5em 1.5em;
        font-size: 0.9em;
    }
    .banner #button {
        position: relative;
        margin-top: 3em;
    }
}



.banner #box #content #text {
    font-size: 2em;
    color: whitesmoke;
	margin: 0;
}

.banner #textio {
    display: flex;
    justify-content: center;
}

.banner #textio ul {
    margin-top: 2em;
}

textarea {
    margin-top: 4em;
    box-sizing: border-box;
    width: 45em;
    height: 20em;
    border-radius: 20px;
    background-color: rgba(0, 0, 0, .6);
    border: 0;
	font-family: "Roboto", Helvetica, sans-serif;
    resize: none;
    transition: transform 0.3s ease;
    transform: translateZ(0);
    font-size: 1.05em;
    color: #ffffff;
    padding: 1em;
    outline: none;
}

textarea:hover {
    transform: scale(1.05) translateZ(0);
}

.banner #button {
    display: flex;
    justify-content: center;
    margin-top: 2.5em;
}

.banner #extract {
    border-radius: 10px;
    border: 0;
}
button {
    width: 10em;
    height: 2em;
    font-size: 1.05em;
    background-color: #1c1d26;
    transition: transform 0.3s ease;
    transform: translateZ(0);
    color: #8b8a8a;
}

button:hover {
    transform: scale(1.14) translateZ(0);
}

button:active {
    transform: scale(0.95);
}
```

