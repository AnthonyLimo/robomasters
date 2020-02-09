import os
from flask import Flask, render_template, redirect, request, jsonify, url_for
import africastalking
from config import Config

# Setting up the Africa's Talking API
username = Config.AT_USERNAME
api_key = Config.AT_APIKEY
_phone_number = Config.AT_PHONE_NUMBER
africastalking.initialize(username, api_key)

# Setup uploading files
# Take in csv and excel files only
# If the file is an excel file, we convert to csv
# Find out how to read csv files
UPLOAD_FOLDER = ""
ALLOWED_EXTENSIONS = {"csv", "xls"}

# Initialize AT Voice service
voice = africastalking.Voice

# Start app
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Set up routes and logic
@app.route("/", methods=["GET", "POST"])
def index():
    number_in_use = _phone_number
    return render_template("index.html", number_in_use=number_in_use)


@app.route("/makecall", methods=["GET", "POST"])
def makecall():
    if request.method == "POST":
        # use the AT SDK to make a call
        # check for the right input for the user
        # possibly convert the input to something AT understands
        # Make multiple calls at the same time
        # I may need to integrate a DBaaS ~> Firebase
        # Check out GCP deployment strategy for Python apps
        pass
    else:
        return render_template("index.html")


# Create the server
# Start in debug mode to make changes on the fly
# try to check out
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT"))
