# app/blog/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, RadioField
from wtforms.validators import DataRequired, Email, EqualTo

class PostForm(FlaskForm):
    """
    Form for user to add or edit a post
    """
    title = StringField('Title', [validators.Length(min=1, max=200)]) 
    
    body = TextAreaField('Body', [validators.Length(min=30)])
    tags = StringField('Tags', [validators.DataRequired()])
    draft = RadioField('Draft', choices=[('True','Is a draft'),('False','Not a draft')])
    submit = SubmitField('Submit')

class CartegoryForm(FlaskForm):
    """
    Form for admin to add or edit cartegories
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')