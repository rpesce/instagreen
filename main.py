import flask_login
from flask import Blueprint, render_template, flash, redirect, request, url_for
from flask_login import login_required, current_user
import datetime
import flask

from app import db
from models import InstagramAccount

year = datetime.datetime.now().strftime("%Y")
main = Blueprint('main', __name__)


@main.route('/')
def index(y=year):
    return render_template('home.html', year=y)


@main.route('/dashboard', methods=['GET'])
@login_required
def profile(y=year):
    user_id = current_user.id
    instagram_accounts = InstagramAccount.query.filter_by(user_id=user_id)
    return render_template('dashboard.html', year=y, name=current_user.name, instagram_accounts=instagram_accounts)


@main.route('/add-instagram', methods=['POST'])
@login_required
def add_instagram():
    if flask.request.method == 'POST':
        instagram_username = request.form.get('instagram_username')
        instagram_password = request.form.get('instagram_password')

        instagram_account = InstagramAccount.query.filter_by(instagram_username=instagram_username).first()

        if instagram_account:
            flash('This Instagram account has already been enabled')
            return redirect(url_for('main.profile'))

        new_instagram_account = InstagramAccount(instagram_username=instagram_username, instagram_password=instagram_password, user_id=current_user.id)
        db.session.add(new_instagram_account)
        db.session.commit()

        flash('Instagram account successfully added')
        return redirect(url_for('main.profile'))
    else:
        return flash('This operation is not authorized')
