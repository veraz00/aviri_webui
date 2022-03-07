
from flask import render_template, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required, current_user  # current user is from flask_login
from app.forms import LoginForm
from app.models import Admin
from app.extensions import db
from . import auth

@auth.route('/login', methods=['POST', 'GET'])  
def login():
    if current_user.is_authenticated:
        return redirect(url_for('image_up.upload_image'))
    form = LoginForm()
    if form.validate_on_submit():  # if it is 'Post'
        username = form.username.data
        password = form.password.data
        remember = form.remember_me.data 
        admin = Admin.query.filter_by(username=username).first()
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)
                flash('Welcome back.', 'info')
                return redirect(url_for('image_up.upload_image'))
                # return redirect(url_for('blog_bp.index'))  # blog_bp.index blue print is blog_bp, route is index
            else:
                flash('Invalid username or password', 'warning')
        else:
            flash('No account', 'warning')
    return render_template('auth/login.html', form = form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))  # where is form, message??