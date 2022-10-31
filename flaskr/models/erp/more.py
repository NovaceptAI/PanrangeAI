import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.models.db import get_db

bp = Blueprint('more', __name__, url_prefix='/more')


@bp.route('/subscription_board', methods=('GET', 'POST'))
def subscription_board():
    return render_template('more/subscription.html')


@bp.route('/settings_board', methods=('GET', 'POST'))
def settings_board():
    return render_template('more/settings.html')
