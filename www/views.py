# Flask imports
from flask import render_template

# App imports
from www import app

@app.route("/")
def index():
    return render_template("/index.html")
