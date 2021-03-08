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
def kanji():
    # Retrieve all kanji
    kanjis = Kanji.query.all()
    return render_template("kanji.html", kanjis=kanjis)
    
    
    
@kanjis.route("/kanji/<int:kanji_id>")
def single_kanji(kanji_id=1):
    kanji = Kanji.query.get_or_404(kanji_id)
    return render_template('single_kanji.html', character=kanji.character, kanji=kanji)
    

@kanjis.route("/kanji/<int:heisig_level>")
def single_heisig_level(heisig_level=1):
    kanji = Kanji.query.get_or_404(heisig_level)
    return render_template('single_heisig_level.html', level=kanji.heisig_level, kanji=kanji)
    