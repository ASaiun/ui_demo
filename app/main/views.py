from flask import render_template, current_app, request, session, redirect, url_for
from .forms import VnfForm
from . import main
from ..models import Vepc


@main.route('/', methods=['GET', 'POST'])
def index():

    form = VnfForm()
    return render_template('index.html', form=form)


@main.route('/info', methods=['GET', 'POST'])
def infoShow():

    if session.get('vepc') == None:
        vepc = Vepc(current_app.config['VEPC_FILE_PATH'])
        vepc_info = vepc.get_vepc()
        session['vepc'] = vepc_info
        session['info_test'] = 'a'

    if request.method == 'POST':

        if request.form['submit'] == "create":
            return redirect(url_for('.infoShow'))

        if request.form['submit'] == "return":
            return redirect(url_for('.infoShow'))

        if request.form['submit'] == "reset":
            session['vepc'] = None
            return redirect(url_for('.infoShow'))

        if request.form['submit'] == "review":
            return render_template('infoReview.html', vepc=session.get('vepc'))

        else:
            num_list = request.form['submit'].split(',')
            session['vepc'][num_list[0]][int(num_list[1])][
                1] = request.form['_target']
            session['info_test'] = 'b'
            return redirect(url_for('.infoShow'))

    return render_template('infoShow.html', vepc=session.get('vepc'))
