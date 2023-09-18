#!/usr/bin/python3 
from flask import Flask, render_template
import redis

r = redis.Redis()
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/on", methods=['POST'])
def on():
    r.publish('sounds',1)
    return render_template("index.html", status='on')


@app.route("/off", methods=['POST'])
def off():
    r.publish('sounds',0)
    return render_template("index.html", status='off')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')