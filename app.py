from flask import Flask
from flask import request

app = Flask(
    __name__, 
    static_folder="static", 
    static_url_path="/static"
)

@app.route("/")
def index():
    return "Welcome to home page."

if __name__ == "__main__":
    app.run()