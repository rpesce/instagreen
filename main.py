from flask import Blueprint, render_template, flash, redirect, request, url_for
from flask_login import login_required, current_user
import datetime
import flask

# from models import InstagramAccount
from app import db

year = datetime.datetime.now().strftime("%Y")
main = Blueprint('main', __name__)


@main.route('/')
def index(y=year):
    return render_template('home.html', year=y)


@main.route('/dashboard')
@login_required
def profile(y=year):
    return render_template('dashboard.html', year=y, name=current_user.name)


@main.route('/add-instagram', methods=['POST'])
@login_required
def add_instagram():
    return render_template('home.html', year=2011)
    # return render_template('home.html', year=2020)
    #if flask.request.method == 'POST':
    #    instagram_username = request.form.get('instagram_username')
    #    instagram_password = request.form.get('instagram_password')

    #    instagram_account = InstagramAccount.query.filter_by(instagram_username=instagram_username).first()

    #    if instagram_account:
    #        flash('This account has already been configured')
    #        return redirect(url_for('main.dashboard'))

    #    new_instagram_account = InstagramAccount(instagram_username=instagram_username, instagram_password=instagram_passwor)
    #    db.session.add(new_instagram_account)
    #    db.session.commit()

    #    return redirect(url_for('main.dashboard'))
    #else:
    #    return flash('This operation is not authorized')
