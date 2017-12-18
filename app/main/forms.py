from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField, StringField, FileRequired
from wtforms.validators import Required


class VnfForm(FlaskForm):
    info = StringField('VnfForm information', validators=[Required()])
    submit = SubmitField('Submit')

class VnfConfigForm(FlaskForm):
    validators = [
        FileRequired(message='There was no file!'),
        FileAllowed(['yml', 'yaml'], message='Must be a yaml file!')
    ]
    VnfConfig = FileField('VnfForm information', validators=validators)


