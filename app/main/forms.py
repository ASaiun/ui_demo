from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField, StringField, FileRequired
from wtforms.validators import Required


class VnfForm(FlaskForm):
    info = StringField('VnfForm information', validators=[Required()])
    submit = SubmitField('Submit')

class VnfConfigForm(FlaskForm):
    VnfConfig = FileField('VnfForm information', validators=[FileRequired()])


