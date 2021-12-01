
#Python flask aplikacija

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")

@app.route("/onama")
def onama():
    return "Ovo je stranica o nama"

if __name__ == "__main__":
    app.run()