from . import bp as auth
from app.models import User
from flask import render_template, flash, request, redirect, url_for
import requests
from app import db
from config import Config
import os
from .forms import LoginForm, RegisterForm, EditProfileForm
from flask_login import login_user, login_required, logout_user, current_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    login = 'hello'
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data

        u = User.query.filter_by(email=email).first()
        
        login_user(u)
        flash('Login Success', 'success')
        return redirect(url_for('index'))
        
    return render_template('login.html.j2', form=form, login=login)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user_data = {
            "first_name" : form.first_name.data.title(),
            "last_name" : form.last_name.data.title(),
            "username" : form.username.data,
            "email": form.email.data.lower(),
            "password" : form.password.data,
        }
        new_user_object = User()
        new_user_object.from_dict(new_user_data)
        new_user_object.save()
        flash("Successfully Registered", "success")
        return redirect(url_for("auth.login"))
    return render_template('register.html.j2', form=form, register=register)

@auth.route('/logout', methods=['GET'])
def logout():
    logout = 'hello'
    logout_user()
    flash('Successfully Logged out', 'primary')
    return redirect(url_for("index"))

@auth.route('/edit_profile', methods=['GET','POST'])
def edit_profile():
    form = EditProfileForm()
    edit = 'hello'
    if request.method == 'POST' and form.validate_on_submit():
        edited_user_data = {
            "first_name" : form.first_name.data.title(),
            "last_name" : form.last_name.data.title(),
            "username" : form.username.data,
            "email": form.email.data.lower(),
            "password":form.password.data,
        }
        user = User.query.filter_by(email = edited_user_data["email"]).first()
        if user and user.email != current_user.email:
            flash('Email is already in use', 'danger')
            return redirect(url_for("auth.edit_profile"))
        
        user = User.query.filter_by(username = edited_user_data["username"]).first()
        if user and user.username != current_user.username:
            flash('Username is already in use', 'danger')
            return redirect(url_for("auth.edit_profile"))
            
        current_user.from_dict(edited_user_data)
        current_user.save()
        flash("Profile Updated", "success")
        return redirect(url_for("index"))
    return render_template('register.html.j2',form=form, edit=edit)