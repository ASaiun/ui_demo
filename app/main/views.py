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
    # print session.get('vepc')
    #print session['vepc'], 22222222222
    #print session.get('info_test'),1
    if session.get('vepc') == None:
        #print "session is None"
        vepc = Vepc(current_app.config['VEPC_FILE_PATH'])
        vepc_info = vepc.get_vepc()
        session['vepc'] = vepc_info
        session['info_test'] = 'a'
        #print "over"

    if request.method == 'POST':
        #print "Post request"
        # print request.form
        #print session.get('info_test'),2
        num_list = request.form['submit'].split(',')
        # print num_list
        # print session['vepc'].get(num_list[0])[int(num_list[1])]
        #print session['vepc']
        session['vepc'][num_list[0]][int(num_list[1])][
            1] = request.form['_target']
        session['info_test'] = 'b'
        #print session.get('info_test'),3
        #print session['vepc'], 1111111111111111111111111111
        return redirect(url_for('.infoShow'))

    return render_template('infoShow.html', vepc=session.get('vepc'))
