#!/usr/bin/python3
""" users routes """
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from app.models.post import Post
from app.forms.users import (RegistrationForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm)
from app.utils.users import save_picture, send_reset_email

users = Blueprint('users', __name__)


from app import db, current_user
@users.route("/register", methods=['GET', 'POST'], strict_slashes=False)
def register():
    """ Renders register form (GET) or creates new user (POST) """
    from app import bcrypt
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'], strict_slashes=False)
def login():
    """ Renders login form (GET) or logs in user (POST) """
    from app import bcrypt
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            from app import app
            app.logger.info('%s logged in successfully', user.username)###
            next_page = request.args.get('next')
            return redirect(next_page if next_page else url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route("/logout", strict_slashes=False)
def logout():
    """ Logs user out """
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'], strict_slashes=False)
@login_required
def account():
    """ Renders account page (GET) or updates account (POST) """
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + db.session.query(User).get(current_user.id).image_file) ##
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@users.route("/user/<string:username>", strict_slashes=False)
def user_posts(username):
    """ Renders user posts page """
    page = request.args.get('page', 1, type=int)
    user = db.session.query(User).filter_by(username=username).first_or_404()
    posts = db.session.query(Post).filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)


@users.route("/reset_password", methods=['GET', 'POST'], strict_slashes=False)
def reset_request():
    """ Renders reset password request form (GET) or sends reset email (POST) """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'], strict_slashes=False)
def reset_token(token):
    """ Renders reset password form (GET) or resets password (POST) """
    from app import bcrypt
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
