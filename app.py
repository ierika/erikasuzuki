import os
from datetime import timedelta

import requests
from unipath import Path
from dotenv import load_dotenv

from flask import Flask
from flask import jsonify
from flask import session
from flask_session import Session


load_dotenv(Path(__file__).ancestor(1).child('.env'))

app = Flask(__name__)
app.config['SESSION_TYPE'] = "filesystem"
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Session(app)
app.debug = True


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
def index():
    """Retrieve JSON response from Treehouse and render"""

    return "Hello world"


@app.route("/profile.json")
def profile():
    """Retrieve Treehouse profile payload"""

    cache_name = "treehouse_profile"

    if session.get(cache_name) is None:
        res = requests.get("https://teamtreehouse.com/codeslikeagirl.json")

        if res.ok:
            session[cache_name] = res.json()

        else:
            return "Could not retrieve Treehouse profile", res.status_code

    return jsonify(session.get(cache_name))


if __name__ == "__main__":
    app.run()
