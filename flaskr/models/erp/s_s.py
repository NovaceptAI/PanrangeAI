import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.models.db import get_db

bp = Blueprint('s_s', __name__, url_prefix='/s_s')


@bp.route('/s_s_board', methods=('GET', 'POST'))
def s_s_board():
    return render_template('sites_stores/s&s.html')

