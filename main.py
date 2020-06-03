from flask import Blueprint, render_template
import datetime


year = datetime.datetime.now().strftime("%Y")
main = Blueprint('main', __name__)


@main.route('/')
def index(y=year):
    return render_template('home.html', year=y)


@main.route('/profile')
def profile(y=year):
    return render_template('profile.html', year=y)

