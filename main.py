from flask import Blueprint, render_template
from flask_login import login_required, current_user
import datetime


year = datetime.datetime.now().strftime("%Y")
main = Blueprint('main', __name__)


@main.route('/')
def index(y=year):
    return render_template('home.html', year=y)


@main.route('/dashboard')
@login_required
def profile(y=year):
    return render_template('dashboard.html', year=y, name=current_user.name)

