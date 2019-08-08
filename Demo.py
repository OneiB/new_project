# Flask class automates the requests
from flask import Flask

# creating a varible from flask
# the variable name gets the name of the python script
# when you execute a python script python assign "__main__" to the file
# But when you import a script to another script the script would be assign "Demo.py"
web_app=Flask(__name__)

# this routes to the desired URL
@web_app.route("/")

# this functions defines what your web page would
def home():
    return "Mission to change the world!"

@web_app.route("/about/")

# this functions defines what your web page would
def about():
    return "Steps to take!"

if __name__ == "__main__":
    web_app.run(debug=True)
