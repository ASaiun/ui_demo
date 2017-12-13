from flask import render_template, current_app
from .forms import VnfForm
from . import main
from ..models import Vepc


@main.route('/', methods=['GET', 'POST'])
def index():
    form = VnfForm()
    return render_template('index.html', form=form)

@main.route('/info', methods=['GET', 'POST'])
def infoShow():

    vepc = Vepc(current_app.config['VEPC_FILE_PATH'])
    vepc_info = vepc.get_vepc()

    return render_template('infoShow.html', vepc=vepc_info)