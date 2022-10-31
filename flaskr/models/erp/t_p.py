import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.models.db import get_db

bp = Blueprint('t_p', __name__, url_prefix='/t_p')


@bp.route('/t_p_board', methods=('GET', 'POST'))
def t_p_board():
    return render_template('tasks_projects/t&p.html')
