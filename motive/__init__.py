from dotenv import load_dotenv
from os import environ
from flask_bcrypt import Bcrypt
from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS, cross_origin

from .models.user import db, User
# Load environment variables

load_dotenv()

database_uri = environ.get('DATABASE_URL')
if 'postgres' in database_uri:
    database_uri = database_uri.replace('postgres:', 'postgresql:')


# Set up the app

app = Flask(__name__, static_folder="client/build", static_url_path="")
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQL_ALCHEMY_TRACK_MODIFICATIONS'),
    SECRET_KEY=environ.get('SECRET')
)

CORS(app)

bcrypt = Bcrypt(app)
db.app = app
db.init_app(app)

############################################################################################################################################################
                                                                #Api Routes#
############################################################################################################################################################
@app.route("/data", methods=["GET"])
@cross_origin()
def index():
    return jsonify({
        "title": "The Motive"
    })

@app.route("/register", methods=["POST"])
@cross_origin()
def register_user():
    email = request.json["email"]
    password = request.json["password"]

    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({"error": "User already exists"}), 409

    hashed_password = bcrypt.generate_password_hash(password)
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
       "id": new_user.id,
       "email":new_user.email
    })

@app.route("/login", methods=["POST"])
@cross_origin()
def login_user():
    email = request.json["email"]
    password = request.json["password"]

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"error": "unauthorised"}), 401 

    if not bcrypt.check_password_hash(user.password, password):
         return jsonify({"error": "unauthorised"}), 401
    return jsonify({
       "id": user.id,
       "email": user.email
    })

############################################################################################################################################################
                                                                #App Routes#
############################################################################################################################################################

@app.route("/")
def serve():
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(debug=True)
