# app/blog/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, ValidationError, RadioField, validators
from wtforms.validators import DataRequired, Email, EqualTo, Length

class ArticleForm(FlaskForm):
    """
    Form for user to add or edit an article
    """
    title = StringField('Title', [validators.Length(min=1, max=200,message='Too short or too long')]) 
    author = StringField('author', [validators.DataRequired()])
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