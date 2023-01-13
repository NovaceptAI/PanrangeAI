import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.models.db import get_db

bp = Blueprint('omnisales', __name__, url_prefix='/omnisales')


@bp.route('/omnisales', methods=('GET', 'POST'))
def omnisales():
    return render_template('omnisales/omnisales.html')

