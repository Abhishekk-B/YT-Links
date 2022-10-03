from flask import render_template, request
from website import app
from website.test import youTubeScrapper, file
# import pandas as pd
import time




@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        product = request.form["product"]
        print(product)
        return render_template("home.html", product = product)
    return render_template("home.html")



    
@app.route("/value/<channel>")
def value(channel):
    videolinks = youTubeScrapper(channel)
    time.sleep(2)
    y = file(channel)
    numbers, titles, links, images, name, view, subscriber = y[0], y[1], y[2], y[3], y[4], y[5], y[6]
    length = len(numbers)
    print("video link scraped")
    return render_template("show.html", product=channel, length=length, titles=titles, images=images,
                                   links=links, numbers=numbers, view=view, subscriber=subscriber)
    # try:
    #     try:
    #         y = file(channel)
    #         numbers, titles, links, images, name, view, subscriber = y[0], y[1], y[2], y[3], y[4], y[5], y[6]
    #         length = len(numbers)
    #         print("video link scraped")
    #         return render_template("show.html", product=channel, length=length, titles=titles, images=images,
    #                                links=links, numbers=numbers, view=view, subscriber=subscriber)
    #     except:
    #         videolinks = youTubeScrapper(channel)
    #         time.sleep(2)
    #         y = file(channel)
    #         numbers, titles, links, images, name, view, subscriber = y[0], y[1], y[2], y[3], y[4], y[5], y[6]
    #         length = len(numbers)
    #         print("video link scraped")
    #         return render_template("show.html", product=channel, length=length, titles=titles, images=images,
    #                                links=links, numbers=numbers, view=view, subscriber=subscriber)
    # except:
    #     return render_template("error.html")


#
#
# @app.route("/comment/<channel>")
# def comment(channel):
#     chann = channel.split(".")[0]
#     try:
#         try:
#             df = pd.read_csv(chann + " videos comments.csv", header=0)
#             data = df.values
#             return render_template("comment.html", csv=data)
#         except:
#             z = file(chann)
#             links = z[2]
#             ytScrapper(links, channel)
#             print("video link scraped")
#             commentFile(chann)
#             time.sleep(2)
#             database(chann)
#             print("Data added")
#             df = pd.read_csv(chann + " videos comments.csv", header=0)
#             data = df.values
#             return render_template("comment.html", csv=data)
#     except:
#         return render_template("error.html")
