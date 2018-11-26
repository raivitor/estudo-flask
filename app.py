# coding: utf-8
from flask import Flask, render_template

app = Flask("project")

@app.route("/")
def home	():
    return render_template("index.html", myname="Rai"), 200

@app.route("/info")
def info():
	return u"Pagina info", 200

app.run()