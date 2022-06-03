from dotenv import load_dotenv
from os import environ
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS, cross_origin

from .database.db import db
# Load environment variables

load_dotenv()

database_uri = environ.get('DATABASE_URL')
if 'postgres' in database_uri:
    database_uri = database_uri.replace('postgres:', 'postgresql:')


# Set up the app

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQL_ALCHEMY_TRACK_MODIFICATIONS')
)

CORS(app)

db.app = app
db.init_app(app)

############################################################################################################################################################
                                                                #Api Routes#
############################################################################################################################################################
@app.route("/data", methods=["GET"])
def index():
    return jsonify({
        "title": "The Motive"
    })


############################################################################################################################################################
                                                                #App Routes#
############################################################################################################################################################

@app.route("/", methods=["GET"])
def serve():
    return "Welcome to the server" 


if __name__ == "__main__":
    app.run(debug=True)

