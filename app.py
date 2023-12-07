from flask import Flask

from routes.index import index_bp
from routes.search import search_bp
from routes.get_data import get_data_bp

# Initialize Flask
app = Flask(
    __name__, 
    static_folder="static", 
    static_url_path="/static"
)

app.register_blueprint(index_bp)
app.register_blueprint(search_bp)
app.register_blueprint(get_data_bp)

if __name__ == "__main__":
    app.run(debug=True)