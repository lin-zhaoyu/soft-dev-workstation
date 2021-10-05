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
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

"""
Predictionss
- The code in the `if` statement will run since we run app.py from the terminal, so __name__ is set to "__main__"
- Same as v2, printing two messages to the terminal
    - First will be: "about to print __name__..."
    - Then: "__main__" since the program is being called directly
- Serves a webpage on localhost port 5000
- Webpage will display "No hablo queso!" when on the "/" root page
- Debug mode will be listed as "on"
    - Maybe some extra information will be printed to the terminal
    - Update code onto the website by auto reloading

Notes
- Webpage acts as expected, continues to run indefinitely
- Debug mode is set on, and gives a debugging PIN
- Messages only appear on the terminal after the webpage is loaded
    - Redeploys page on changes to the file
- Warns on being a "development server" and not to actually use for production
- No HTML tags for the message, just a raw string "No hablo queso!"
- Terminal displays HTTP GET Requests every time the page is loaded
"""
