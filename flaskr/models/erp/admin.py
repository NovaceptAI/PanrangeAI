from flask import (
    Blueprint, render_template
)

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/admin_board', methods=('GET', 'POST'))
def admin_board():
    return render_template('admin/admin_board.html')


@bp.route('/add_user', methods=('GET', 'POST'))
def add_user():
    return render_template('admin/add_user.html')
