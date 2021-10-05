"""
Blind Elmo: Lucas Lee (Lewis Cass), Zhaoyu Lin, Lucas Tom Wong (LTW)
SoftDev
k10 -- Futher Thoughts on Flask App Varations
2021-10-05
"""

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()


"""
Predictions
- Same as v0 without a message to the terminal
- Serves a webpage on localhost port 5000
- Webpage will display "No hablo queso!" when on the "/" root page

Notes
- Webpage acts as expected, continues to run indefinitely
- Warns on being a "development server" and not to actually use for production
- No HTML tags for the message, just a raw string "No hablo queso!"
- Terminal displays HTTP GET Requests every time the page is loaded
"""
