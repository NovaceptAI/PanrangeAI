import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.models.db import get_db

bp = Blueprint('marketing', __name__, url_prefix='/marketing')


@bp.route('/marketing_board', methods=('GET', 'POST'))
def marketing_board():
    return render_template('marketing/marketing.html')


@bp.route('/market_board', methods=('GET', 'POST'))
def market_board():
    return render_template('market/market.html')


@bp.route('/dev_resources', methods=('GET', 'POST'))
def dev_resources():
    return render_template('market/dev_resources.html')
