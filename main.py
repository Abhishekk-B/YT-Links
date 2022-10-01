from flask import Flask, render_template, request
import pandas as pd
import time
from yt import youTubeScrapper, file

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        product = request.form["product"]
        print(product)
        return render_template("home.html", product=product)
    return render_template("home.html")

#
@app.route("/value/<channel>")
def value(channel):

    try:
        videolinks = youTubeScrapper(channel)
        y = file(channel)
        numbers, titles, links, name, view, subscriber = y[0], y[1], y[2], y[3], y[4], y[5]
        length = len(numbers)
        print("video link scraped")
        return render_template("show.html", product=channel, length=length, titles=titles, links=links, numbers=numbers,
                               view=view, subscriber=subscriber)

    except:
        print("error")
    return render_template("error.html")


if __name__=="__main__":
    app.run(debug=True)

