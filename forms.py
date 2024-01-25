from flask_wtf import FlaskForm
from wtforms import StringField, URLField, IntegerField, BooleanField
from wtforms.validators import InputRequired, URL, AnyOf, NumberRange, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'], message='Invalid species')])
    photo_url = URLField("Photo URL", validators=[Optional(), URL(message='Invalid URL')])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message='Age must be between 0 and 30')])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """Form for edditing pet info"""

    photo_url = URLField("Photo URL", validators=[Optional(), URL(message='Invalid URL')])
    notes = StringField("Notes")
    available = BooleanField("Available?")
