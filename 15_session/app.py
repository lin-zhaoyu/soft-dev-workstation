# BlueGreen (Edwin Zheng, Shriya Anand, Zhaoyu Lin)
# SoftDev
# K14: Form and Function
# Oct 14, 2021

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session
from flask import make_response
import random

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. Can you predict which?
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests. Process results.
PROTIP: Insert your own in-line comments wherever they will help your future self and/or current teammates understand what is going on.
'''

@app.route("/") #,methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():

    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)


    username = "u"
    password = "1"
    list = ["greetings"]
    greetings = ['Hello Travelers','Welcome Travelers','Bonjour Travelers']
    greeting = str(random.choices(greetings))
    response = ""

    if(request.args['username'] != username):
        response = "incorrect username +++" #line break
    if(request.args['password'] != password):
        response += "incorrect password"

    if(response == ""):
        response =  "logged in"
    #cookies
    resp = make_response(request.args['username'])
    resp.set_cookie('userID', request.args['username'])
    print(request.cookies.get('userID'))
    return resp
    # render_template('response.html',response = response,
    # request_method=request.args['sub1'],greet=greeting)
    #return request.args['sub1']
    #return request.args['username']  #response to a form submission
    #return "Hello"


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
