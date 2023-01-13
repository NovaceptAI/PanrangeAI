import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.models.db import get_db

bp = Blueprint('finance', __name__, url_prefix='/finance')


@bp.route('/finance_board', methods=('GET', 'POST'))
def inventory_dashboard():
    return render_template('finance/finance.html')


@bp.route('/key_data', methods=('GET', 'POST'))
def key_data_board():
    return render_template('finance/key_data.html')


@bp.route('/reporting', methods=('GET', 'POST'))
def reporting_data():
    return render_template('finance/reporting.html')


@bp.route('/invoice_form', methods=('GET', 'POST'))
def invoice_form():
    return render_template('finance/invoice_form.html')
