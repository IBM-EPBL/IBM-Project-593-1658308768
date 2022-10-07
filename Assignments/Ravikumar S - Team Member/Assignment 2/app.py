

from flask import Flask, render_template
from main import main


app = Flask(__name__)
app.register_blueprint(main,url_prefix="/admin")
@app.route("/")
def hello_world():
    return "<p>test</p>"
if __name__ == "__main__":
    app.run()
