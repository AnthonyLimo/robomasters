# Create a class that exports constants
import os


class Config(object):
    AT_USERNAME = "njugunamadeit"
    AT_APIKEY = "dc23f71c347411b29498bd33c1d0ccf36210bc44d3370ee0920cd5254a01720d"
    AT_PHONE_NUMBER = "+254711082936"
    SECRET_KEY = os.environ.get("SECRET_KEY")
