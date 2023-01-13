import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.models.db import get_db

bp = Blueprint('hrm', __name__, url_prefix='/hrm')


@bp.route('/hrm_board', methods=('GET', 'POST'))
def hrm():
    return render_template('hrm/hrm.html')


@bp.route('/ats', methods=('GET', 'POST'))
def ats():
    return render_template('hrm/ats.html')


@bp.route('/manpower', methods=('GET', 'POST'))
def manpower():
    return render_template('hrm/manpower_dashboard.html')


@bp.route('/requisition', methods=('GET', 'POST'))
def requisition():
    return render_template('hrm/manpower_requisition.html')


@bp.route('/joblist', methods=('GET', 'POST'))
def joblist():
    return render_template('hrm/job_list.html')


@bp.route('/jobform', methods=('GET', 'POST'))
def job_form():
    return render_template('hrm/job_posting.html')
