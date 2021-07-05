from flask import Blueprint, render_template, url_for

main = Blueprint('main', __name__)


@main.route('/')
def index():
    print("Index Page")
    return render_template('index.html')

@main.route('/profile')
def profile():
    print("Profile Page")
    return render_template('profile.html')