from flask import Flask
from flask import render_template
from redispak import showset, gethash, HASH
app = Flask(__name__)

@app.route("/")
def hello():
    name = "blog"
    works = showset(name)
    print(works)

    return render_template("index.html", list = works)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5001')


