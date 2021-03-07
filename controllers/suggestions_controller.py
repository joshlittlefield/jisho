from models.Suggestion import Suggestion
from models.User import User
from main import db
from schemas.SuggestionSchema import suggestion_schema, suggestions_schema
from flask import Blueprint, request, jsonify, abort, render_template, url_for, flash , redirect
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload
from forms import RegistrationForm, LoginForm, PostForm
from flask_login import login_user, current_user, logout_user, login_required


suggestions = Blueprint('suggestions', __name__)

@suggestions.route("/")
@suggestions.route("/home")
def home():
    # Retrieve all suggestions
    suggestions = Suggestion.query.options(joinedload("user")).all()
    return render_template("home.html", suggestions=suggestions)
    



@suggestions.route("/suggestion/new", methods=['GET', 'POST'])
@login_required
def new_suggestion():
    form = PostForm()
    if form.validate_on_submit():
        suggestion = Suggestion(title=form.title.data, content=form.content.data, user=current_user)
        db.session.add(suggestion)
        db.session.commit()
        flash('Your Suggestion has been created!', 'success')
        return redirect(url_for('suggestions.home'))
    return render_template('create_suggestion.html', title='New Suggestion', form=form, legend='New Suggestion')


@suggestions.route("/suggestion/<int:suggestion_id>")
def suggestion(suggestion_id):
    suggestion = Suggestion.query.get_or_404(suggestion_id)
    return render_template('suggestion.html', title=suggestion.title, suggestion=suggestion)


@suggestions.route("/suggestion/<int:suggestion_id>/update", methods=['GET', 'POST'])
@login_required
def update_suggestion(suggestion_id):
    suggestion = Suggestion.query.get_or_404(suggestion_id)
    if suggestion.user != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        suggestion.title = form.title.data
        suggestion.content = form.content.data
        db.session.commit()
        flash('Your suggestion has been updated!', 'success')
        return redirect(url_for('suggestions.suggestion', suggestion_id=suggestion.id))
    elif request.method == 'GET':
        form.title.data = suggestion.title
        form.content.data = suggestion.content
    return render_template('create_suggestion.html', title='Update Suggestion',
                           form=form, legend='Update Suggestion')


@suggestions.route("/suggestion/<int:suggestion_id>/delete", methods=['POST'])
@login_required
def delete_suggestion(suggestion_id):
    suggestion = Suggestion.query.get_or_404(suggestion_id)
    if suggestion.user != current_user:
        abort(403)
    db.session.delete(suggestion)
    db.session.commit()
    flash('Your suggestion has been deleted!', 'success')
    return redirect(url_for('suggestions.home'))

