# Not production code
# Spaghetti code to get things up and running
# If you want to see prod code, change the branh to prod
from app import app
import os
from flask import Flask, render_template, redirect, request, jsonify, url_for
import africastalking
from config import Config

# We need to find a way of tracking sessions
# Flask has an inbuilt session manager
# Allows us to also manage login/logout

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
    # Create a dictionary to hold context variables for the flask route method
    # Pass in the context as args within the render_template() method
    context = {
        'number_in_use': _phone_number,
    }
    return render_template("index.html", **context)


@app.route("/makecall", methods=["GET", "POST"])
def makecall():
    if request.method == "POST":
        # use the AT SDK to make a call
        # check for the right input for the user
        # possibly convert the input to something AT understands
        # Make multiple calls at the same time
        # I may need to integrate a DBaaS ~> Firebase
        # Check out GCP deployment strategy for Python apps
        # pass

        # Combine contact list or provided number into dictionary
        # Send it to AT as a dict
        # Rethink data sources

        contact_list = []

        try:
            resp = voice.call(callFrom=_phone_number, callTo=contact_list)
            print(resp)
        except Exception as e:
            print(
                f"Something went wrong while trying to execute these calls: ${e}")

    else:
        return render_template("index.html")


# Create the server
# Start in debug mode to make changes on the fly
# try to check out
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=os.environ.get("PORT"))
