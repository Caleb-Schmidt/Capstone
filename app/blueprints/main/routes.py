from . import bp as main
from flask import render_template, request, redirect, url_for, flash
import requests
from flask_login import current_user, login_required
from config import Config
import os
from .forms import PostForm, EditPostForm
from app.models import Post, User


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

@main.route('/admins', methods=['GET', 'POST'])
def show_admins():
    users = User.query.all()
    sorted_users = sorted(users, key=lambda x: x.last_name)
    return render_template('admins.html.j2', users=sorted_users)

# @main.route('/admins_update<int:id>', methods=['GET', 'POST'])
# def admin_status(id):
#     user = User.query.get(id)
#     if not user.is_admin:
#         user.make_admin()
#     else:
#         user.remove_admin()
#     users = User.query.all()
#     return render_template('admins.html.j2', users=users)

@main.route('/assign_admin<int:id>', methods=['GET', 'POST'])
def assign_admin(id):
    admin = User.query.get(id)
    admin.make_admin()
    users = User.query.all()
    return render_template('admins.html.j2', users=users)

@main.route('/assign_user<int:id>', methods=['GET', 'POST'])
def assign_user(id):
    user = User.query.get(id)
    user.remove_admin()
    users = User.query.all()
    return render_template('admins.html.j2', users=users)

@main.route('/admin_pending<int:id>', methods=['GET', 'POST'])
def admin_pending(id):
    user = User.query.get(id)
    full_name = user.first_name + user.last_name
    pass

@main.route('/delete_user/<int:id>', methods=['GET', 'POST'])
def delete_user(id):
    user = User.query.get(id)
    user.delete()
    users = User.query.all()
    return render_template('admins.html.j2', users=users)
