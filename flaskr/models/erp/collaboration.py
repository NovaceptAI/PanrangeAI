import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.models.db import get_db

bp = Blueprint('colab', __name__, url_prefix='/colab')


@bp.route('/c_c', methods=('GET', 'POST'))
def c_c():
    return render_template('collaboration/c&c.html')


@bp.route('/calender', methods=('GET', 'POST'))
def calender():
    return render_template('collaboration/calender.html')


@bp.route('/drive', methods=('GET', 'POST'))
def drive():
    return render_template('collaboration/drive.html')


@bp.route('/feed', methods=('GET', 'POST'))
def feed():
    return render_template('collaboration/feed.html')


@bp.route('/online_docu', methods=('GET', 'POST'))
def online_docu():
    return render_template('collaboration/online_docu.html')


@bp.route('/webmail', methods=('GET', 'POST'))
def webmail():
    return render_template('collaboration/webmail.html')


@bp.route('/workgroup', methods=('GET', 'POST'))
def workgroup():
    return render_template('collaboration/workgroup.html')
