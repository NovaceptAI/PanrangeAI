import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('landing', __name__)


@bp.route('/', methods=('GET', 'POST'))
def landing():
    return render_template('landing/landing_page.html')


@bp.route('/web_index_web', methods=('GET', 'POST'))
def web_index():
    return render_template('landing/web_index_web.html')


@bp.route('/erp_dashboard', methods=('GET', 'POST'))
def erp_index():
    return render_template('landing/erp_dashboard.html')
