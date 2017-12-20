from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import SubmitField, FileField, StringField, SelectField
from wtforms.validators import Required, Optional


class VnfForm(FlaskForm):
    info = StringField('VnfForm information', validators=[Required()])
    submit = SubmitField('Submit')

class VnfConfigForm(FlaskForm):
    validators = [
        FileRequired(message='There was no file!'),
        FileAllowed(['yml', 'yaml'], message='Must be a yaml file!')
    ]
    VnfConfig = FileField('VnfForm information', validators=validators)

class InfoForm(FlaskForm):
    # vnf_type = SelectField('VNF type', choices= ['epg', 'sapc', 'wmg'])
    vnf_type = SelectField('VNF type', choices=[('epg', 'EPG'), ('sapc', 'SAPC'), ('wmg', 'WMG')], validators=[Required()])

    vdp_info = StringField('VDP name', validators=[Required()])


    validators = [
        FileRequired(message='There was no file!'),
        FileAllowed(['yml', 'yaml'], message='Must be a yaml file!')
    ]
    VnfConfig = FileField('VNF config', validators=validators)

    submit = SubmitField('Submit')
