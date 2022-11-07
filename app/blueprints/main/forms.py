from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    title = StringField('Subject',validators=[DataRequired()])
    body = StringField('Message',validators=[DataRequired()])
    author = StringField('Your Name',validators=[DataRequired()])
    submit = SubmitField('Submit')