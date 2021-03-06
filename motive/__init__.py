from dotenv import load_dotenv
from os import environ
import redis
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask import Flask, send_from_directory, jsonify, request, session
from flask_cors import CORS
from werkzeug import exceptions

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
    SECRET_KEY=environ.get('SECRET'),
    
    SESSION_TYPE = "redis",
    SESSION_PERMANENT = False,
    SESSION_REDIS = redis.from_url("redis://:pd5b772b513d356ff7c0dd1514db19557505e48a390959bd4c93242382ad159ef@ec2-54-194-35-138.eu-west-1.compute.amazonaws.com:31459"),
    SESSION_COOKIE_SECURE = True
)

CORS(app, supports_credentials=True)

bcrypt = Bcrypt(app)
server_session = Session(app)
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

@app.route("/@me")
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorised"}), 401
    
    user = User.query.filter_by(id=user_id).first()
    return jsonify({
        "id": user.id,
       "email": user.email
    })

@app.route("/register", methods=["POST"])
def register_user():
    email = request.json["email"]
    password = request.json["password"]

    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({"error": "User already exists"}), 409

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
       "id": new_user.id,
       "email":new_user.email
    })


@app.route("/login", methods=["POST"])
def login_user():
    email = request.json["email"]
    password = request.json["password"]

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"error": "Unauthorised"}), 401 

    if not bcrypt.check_password_hash(user.password, password):
         return jsonify({"error": "Unauthorised"}), 401

    session["user_id"] = user.id

    return jsonify({
       "id": user.id,
       "email": user.email
    })

############################################################################################################################################################
                                                                #App Routes#
############################################################################################################################################################

@app.errorhandler(exceptions.NotFound)
def serve(err):
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(debug=False)
