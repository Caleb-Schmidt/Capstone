from . import bp as main
from flask import render_template, request, redirect, url_for
import requests
from config import Config
import os

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
    messages='hello'
    return render_template('messages.html.j2', messages=messages)

@main.route('/profile', methods=['GET', 'POST'])
def profile():
    profile='hello'
    return render_template('profile.html.j2', profile=profile)

@main.route('/create_post', methods=['GET', 'POST'])
def create_post():
    return render_template('create_post.html.j2')