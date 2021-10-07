"""
Blind Elmo: Lucas Lee (Lewis Cass), Zhaoyu Lin, Lucas Tom Wong (LTW)
SoftDev
k10 -- Futher Thoughts on Flask App Varations
2021-10-05
"""


from flask import Flask
app = Flask(__name__)

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q3: Will this appear anywhere? How u know?

app.run()  # Q4: Where have you seen similar construcs in other languages?

"""
Predictions
- Serves a webpage on localhost port 5000
- Will print out __main__ on the terminal
    - __name__ is set to __main__ since app.py is being called directly
- Webpage will display "No hablo queso!"

Notes
- Webpage acts as expected, continues to run indefinitely
- __main__ is printed to the terminal after page is loaded
- Warns on being a "development server" and not to actually use for production
- No HTML tags for the message, just a raw string "No hablo queso!"
- Terminal displays HTTP GET Requests every time the page is loaded
"""
