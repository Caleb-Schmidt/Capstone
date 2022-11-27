from app import db, login
from flask_login import UserMixin, current_user
from datetime import datetime as dt, timedelta
import secrets
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    token = db.Column(db.Integer, unique=True, index=True)
    is_admin = db.Column(db.Boolean, default=False)

    def get_token(self, exp=86400):
        current_time = dt.utcnow()

        if self.token and self.token.exp > current_time + timedelta(seconds=60):
            return self.token

        self.token = secrets.token_urlsafe(32)
        self.token_exp = current_time + timedelta(seconds=exp)
        self.save()
        return self.token
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def from_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email= data['email']
        self.password = self.hash_password(data['password'])

    def hash_password(self, original_password):
        return generate_password_hash(original_password)

    def check_hashed_password(self, login_password):
        return check_password_hash(self.password, login_password)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def make_admin(self):
        self.is_admin = True
        db.session.commit()

    def remove_admin(self):
        self.is_admin = False
        db.session.commit()
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    img = db.Column(db.String)
    body = db.Column(db.String(500))
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    date_modified = db.Column(db.DateTime, onupdate=dt.utcnow)

    def __repr__(self):
        return f'<Post: {self.id} | {self.body[:15]}>'

    def edit(self, new_body):
        self.body = new_body

    def to_dict(self):
        return{
            'id':self.id,
            'body':self.body,
            'created_on':self.created_on,
            'date_modified':self.date_modified,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Event(db.Model):
    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    img = db.Column(db.String)
    body = db.Column(db.String(500))
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    date_modified = db.Column(db.DateTime, onupdate=dt.utcnow)

    def __repr__(self):
        return f'<Event: {self.id} | {self.body[:15]}>'

    def edit(self, new_body):
        self.body = new_body

    def to_dict(self):
        return{
            'id':self.id,
            'body':self.body,
            'created_on':self.created_on,
            'date_modified':self.date_modified,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()