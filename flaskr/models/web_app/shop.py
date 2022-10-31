from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.models.db import get_db

bp = Blueprint('web_app', __name__, url_prefix='/web_app')


@bp.route('/shop', methods=('GET', 'POST'))
def shop():
    return render_template('web_app/web_shop.html')


@bp.route('/bestsellers', methods=('GET', 'POST'))
def bestsellers():
    return render_template('web_app/bestsellers.html')


@bp.route('/new_releases', methods=('GET', 'POST'))
def new_releases():
    return render_template('web_app/new_releases.html')


@bp.route('/product_details', methods=('GET', 'POST'))
def product_details():
    return render_template('web_app/product_details.html')


@bp.route('/customer_service', methods=('GET', 'POST'))
def customer_service():
    return render_template('web_app/customer/customer_service.html')


@bp.route('/orders', methods=('GET', 'POST'))
def orders():
    return render_template('web_app/customer/orders.html')


@bp.route('/all_appliances', methods=('GET', 'POST'))
def all_appliances():
    return render_template('web_app/all_appliances.html')


@bp.route('/all_refrigerators', methods=('GET', 'POST'))
def refrigerators():
    return render_template('web_app/appliances/refrigerators.html')


@bp.route('/refrigerators_bestsellers', methods=('GET', 'POST'))
def refrigerators_bestsellers():
    return render_template('web_app/appliances/refrigerators_bestsellers.html')


@bp.route('/refrigerators_new', methods=('GET', 'POST'))
def refrigerators_new():
    return render_template('web_app/appliances/refrigerators_new.html')


@bp.route('/all_acs', methods=('GET', 'POST'))
def acs():
    return render_template('web_app/appliances/all_acs.html')
