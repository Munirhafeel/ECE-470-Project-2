from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

## Blueprint for routes
views = Blueprint('views', __name__)

#decorator
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

