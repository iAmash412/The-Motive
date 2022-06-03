from flask import Blueprint, request, render_template
from flask_cors import CORS, cross_origin
from ..database.db import db
from ..models.listing import Listing

api_routes = Blueprint("api", __name__)

@api_routes.route("/", methods=["GET"])
@cross_origin()
def index():
    return {
        "title": "The Motive"
    }
