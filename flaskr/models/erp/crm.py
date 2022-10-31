import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.models.db import get_db

bp = Blueprint('crm', __name__, url_prefix='/crm')


@bp.route('/crm_board', methods=('GET', 'POST'))
def crm_board():
    return render_template('crm/crm.html')

