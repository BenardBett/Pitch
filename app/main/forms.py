 
from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required, Email

class UpdateProfile (FlaskForm):
    """
    Class to update user profile
    """
    bio = TextAreaField ('Write something about you...', validators = [Required()])
    submit = SubmitField ('Submit')