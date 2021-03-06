from models.Kanji import Kanji
from models.User import User
from main import db
from schemas.KanjiSchema import kanji_schema, kanjis_schema
from flask import Blueprint, request, jsonify, abort, render_template, url_for, flash , redirect
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload
from forms import RegistrationForm, LoginForm, PostForm
from flask_login import login_user, current_user, logout_user, login_required


kanjis = Blueprint('kanjis', __name__)


@kanjis.route("/kanji")
@login_required
def kanji(kanji_id):
    # Retrieve all suggestions
    kanjis = Kanji.query.get_or_404(kanji_id)
    return render_template("kanji.html", kanjis=kanjis)
    