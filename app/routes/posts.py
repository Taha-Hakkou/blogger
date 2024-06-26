#!/usr/bin/python3
""" posts routes """
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import login_required
from app import db, current_user
from app.models.post import Post
from app.forms.posts import PostForm

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'], strict_slashes=False)
@login_required
def new_post():
    """ Renders new post form (GET) or creates new post (POST) """
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/post/<int:post_id>", strict_slashes=False)
def post(post_id):
    """ Renders post page """
    post = db.session.query(Post).get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'], strict_slashes=False)
@login_required
def update_post(post_id):
    """ Renders update post form (GET) or updates post (POST) """
    post = db.session.query(Post).get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'], strict_slashes=False)
@login_required
def delete_post(post_id):
    """ Deletes post """
    post = db.session.query(Post).get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))