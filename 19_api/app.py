# HaroldHuggers Zhao Yu Lin, William Chen
# SoftDev
# K19 -- A RESTful Journey Skyward
# 11-24-2021

from flask import Flask, render_template, request
import urllib, json

app = Flask(__name__)    #create Flask object

@app.route("/") #, methods=['GET', 'POST'])
def display_img():
    with open('key_nasa.txt', 'r') as file:
        api_key = file.read()
        #print(api_key)

    data = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=" + api_key)
    #print(data)
    info = data.read()
    #print(info)
    img = (json.loads(info))["url"]
    return render_template( 'main.html', img = img)

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
