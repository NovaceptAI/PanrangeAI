import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.models.db import get_db

bp = Blueprint('inventory', __name__, url_prefix='/inventory')


@bp.route('/inventory_dashboard', methods=('GET', 'POST'))
def inventory_dashboard():
    return render_template('inventory_management/inventory_board.html')


@bp.route('/products', methods=('GET', 'POST'))
def products():
    return render_template('inventory_management/product/products.html')


@bp.route('/product_form', methods=('GET', 'POST'))
def product_form():
    return render_template('inventory_management/product/product_form.html')


@bp.route('/product_slider', methods=('GET', 'POST'))
def product_slider():
    return render_template('inventory_management/product/product_slider.html')


@bp.route('/product_catalog', methods=('GET', 'POST'))
def product_catalog():
    return render_template('inventory_management/product/product_catalog.html')


@bp.route('/add_product', methods=('GET', 'POST'))
def add_product():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
    return render_template('inventory_management/product/product_form.html')


@bp.route('/sales_order', methods=('GET', 'POST'))
def sales_order():
    return render_template('inventory_management/sales/sales_order.html')


@bp.route('/transfers', methods=('GET', 'POST'))
def transfers():
    return render_template('inventory_management/transfers/transfers.html')


@bp.route('/write_off', methods=('GET', 'POST'))
def write_off():
    return render_template('inventory_management/write_offs/write_offs.html')


@bp.route('/analytics', methods=('GET', 'POST'))
def analytics():
    return render_template('inventory_management/analytics/analytics.html')
