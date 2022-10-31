import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.models.db import get_db

bp = Blueprint('company', __name__, url_prefix='/company')


@bp.route('/company_board', methods=('GET', 'POST'))
def crm_board():
    return render_template('company/company.html')

