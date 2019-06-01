import datetime

from flask import Flask, render_template, json, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    pageTitle = "Is it New Years day yet?"
    now = datetime.datetime.now()
    todayNewYears = now.month == 1 and now.day == 1
    return render_template("index.html", todayNewYears=todayNewYears, pageTitle=pageTitle )


@app.route("/authors", methods=["GET", "POST"])
def authors():
    if session.get("names") is None:
        session["names"] = []
    if request.method == "GET":
        return render_template("authors.html", names=session["names"])
    else:
        name = request.form.get("name")
        if name:
            session["names"].append(name)
        return render_template("authors.html", names=session["names"])

@app.route("/test")
def test():
    pageTitle = "Does this work?"
    cardContent = [
        {'order': 0, 'type': "text", 'text':"hello there!"},
        {'order': 1, 'type': "video", 'uri': "https://www.youtube.com/watch?v=kxRRuM99yg0"},
        {'order': 2, 'type': "picture", 'alt': "Front of Dongguksa Temple", 'uri': "https://farm2.staticflickr.com/1939/43640256040_a699d0f07a_k.jpg"}
        ]
    return render_template("test_for_front_end.html",cardContent=cardContent, pageTitle=pageTitle )
