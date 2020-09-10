from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, TextAreaField


class PictureForm(FlaskForm):
    picture = FileField('Upload picture', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Upload')
