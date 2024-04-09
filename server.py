from flask import Flask, render_template
from flask_app import app


@app.get("/")
def index():
    """This route renders the home page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)
