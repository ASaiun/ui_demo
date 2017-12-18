from flask import render_template, current_app, request, session, redirect, url_for, flash
from .forms import VnfForm, VnfConfigForm
from . import main
from ..models import Vepc
from werkzeug.utils import secure_filename


@main.route('/', methods=['GET', 'POST'])
def index():
    def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.ALLOWED_EXTENSIONS
    form = VnfForm()
    return render_template('index.html', form=form)
    if methods = 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


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
