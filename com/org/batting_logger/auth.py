from flask import Blueprint, render_template, url_for

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    print("SignUp Page")
    return render_template('signup.html')


@auth.route('/login')
def login():
    print("Login Page")
    return render_template('login.html')

@auth.route('/logout')
def logout():
    print("LogOut Page")
    return render_template('index.html')