from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    img = StringField('Image URL')
    body = StringField('Message',validators=[DataRequired()])
    submit = SubmitField('Submit')

class EditPostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    img = StringField('Image URL')
    body = StringField('Message',validators=[DataRequired()])
    submit = SubmitField('Submit')