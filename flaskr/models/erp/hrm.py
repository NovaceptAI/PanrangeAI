import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.models.db import get_db

bp = Blueprint('hrm', __name__, url_prefix='/hrm')


@bp.route('/hrm_board', methods=('GET', 'POST'))
def hrm():
    return render_template('hrm/hrm.html')

