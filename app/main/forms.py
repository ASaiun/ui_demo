from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import Required


class VnfForm(FlaskForm):
    info = StringField('VnfForm information', validators=[Required()])
    submit = SubmitField('Submit')

		