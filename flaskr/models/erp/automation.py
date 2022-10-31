import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.models.db import get_db

bp = Blueprint('automation', __name__, url_prefix='/automation')


@bp.route('/automation_board', methods=('GET', 'POST'))
def automation_board():
    return render_template('automation/automation.html')

