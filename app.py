# coding: utf-8
from flask import Flask, render_template

app = Flask("project")

@app.route("/")
def home	():
    return render_template("index.html", myname="Rai"), 200

@app.route("/info")
@app.route("/info/<name>")
@app.route("/info/<name>/<age>")
def info(name = None, age = None):
	return u"Name: {}<br>Age: {}".format(name, age), 200

app.run()