from flask import Blueprint, request, render_template
from flask_cors import CORS, cross_origin
from ..database.db import db
from ..models.listing import Listing

main_routes = Blueprint("Main", __name__)

@main_routes.route("/", methods=["GET", "POST"])
@cross_origin
def server():
    return send_from_directory(app.static_folder, "index.html")
