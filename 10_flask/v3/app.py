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
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()


"""
Predictionss
- Same as v2, printing two messages to the terminal
    - First will be: "about to print __name__..."
    - Then: "__main__" since the program is being called directly
- Serves a webpage on localhost port 5000
- Webpage will display "No hablo queso!" when on the "/" root page
- Debug mode will be listed as "on"
    - Maybe some extra information will be printed to the terminal

Notes
- Webpage acts as expected, continues to run indefinitely
- Debug mode is set on, and gives a debugging PIN
    - Redeploys page on changes to the file
- Messages only appear on the terminal after the webpage is loaded
- Warns on being a "development server" and not to actually use for production
- No HTML tags for the message, just a raw string "No hablo queso!"
- Terminal displays HTTP GET Requests every time the page is loaded
"""
