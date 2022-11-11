from . import bp as main
from flask import render_template, request, redirect, url_for, flash
import requests
from flask_login import current_user, login_required
from config import Config
import os
from .forms import PostForm, EditPostForm
from app.models import Post

@main.route('/events', methods=['GET', 'POST'])
def events():
    events='hello'
    return render_template('events.html.j2', events=events)

@main.route('/music', methods=['GET', 'POST'])
def music():
    music='hello'
    return render_template('music.html.j2', music=music)

@main.route('/devotions', methods=['GET', 'POST'])
def devotions():
    devotions='hello'
    return render_template('devotions.html.j2', devotions=devotions)

@main.route('/messages', methods=['GET', 'POST'])
def messages():
    message='hello'
    return render_template('messages.html.j2', message=message)

@main.route('/profile', methods=['GET', 'POST'])
def profile():
    profile='hello'
    return render_template('profile.html.j2', profile=profile)

@main.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data
        img = form.img.data
        body = form.body.data
        new_post = Post(title=title, img=img, body=body)
        new_post.save()
        flash('Post Created','success')
        return redirect(url_for('index'))
    return render_template('create_post.html.j2', form=form)

@main.route('/edit_post/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    edited_post = Post.query.get(id)
    if request.method == 'POST':
        edited_post.edit(request.form.get('body'))
        edited_post.save()
        flash('Post has been edited', 'success')

        return redirect(url_for('index'))
    return render_template('edit_post.html.j2', post=edited_post)

@main.route('/delete_post/<int:id>', methods=['GET', 'POST'])
def delete_post(id):
    post = Post.query.get(id)
    post.delete()
    return redirect(url_for('index'))

@main.route('/pending/<int:id>', methods=['GET', 'POST'])
def pending(id):
    post = Post.query.get(id)
    return render_template('pending.html.j2', post=post)