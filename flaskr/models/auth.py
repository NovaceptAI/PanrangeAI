import functools
import math
import random

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from twilio.rest import Client

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response, jsonify)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.models.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/mobile_login', methods=('GET', 'POST'))
def mobile_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        web_users = db.users.count_documents({"username": username, "password": password})

        if not web_users:
            return jsonify({"msg": "Bad username or password"}), 401

        access_token = create_access_token(identity=username)

        return jsonify(access_token=access_token)


@bp.route('/mobile_register', methods=('GET', 'POST'))
def mobile_register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        phone = request.form['phone']
        email = request.form['email']
        db = get_db()
        web_users = db.users.count_documents({"username": username})

        if web_users == 0:
            db.users.insert_one({"username": username,
                                 "password": password,
                                 "mail": email,
                                 "phone": phone})
            status = 200
            msg_code = "SUCCESS"
            message = "USER CREATED"
        else:
            status = 401
            msg_code = "FAILED"
            message = "USERNAME TAKEN"

        response = make_response(
            jsonify(
                {
                    "status": status,
                    "msg_code": msg_code,
                    "msg": message
                }
            ),
            401,
        )
        response.headers["Content-Type"] = "application/json"
        return response


@bp.route('/otp_register', methods=('GET', 'POST'))
def otp_register():
    if request.method == 'POST':
        phone = request.args.get("phone")
        digits = "0123456789"
        OTP = ""
        for i in range(6):
            OTP += digits[math.floor(random.random() * 10)]

        account_sid = 'ACac764d6b630147d2c7b44616eb9f84d6'
        auth_token = '5070483c1bba6aff449eacb69395ce05'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            messaging_service_sid='MG0fee8024a712c8f8a2550553460e25e7',
            body='Your Panrange verification code is: '+OTP,
            to=phone
        )
        status = 200
        msg_code = "SUCCESS"
        message = "OTP SENT"
        response = make_response(
            jsonify(
                {
                    "status": status,
                    "msg_code": msg_code,
                    "msg": message,
                    "data": {
                                "generated_otp": OTP
                            }
                }
            ),
            401,
        )
        response.headers["Content-Type"] = "application/json"
        return response


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        # Web App Login
        web_user = db.admin_creds.find({"username": username, "type": "web"})
        web_users = db.admin_creds.count_documents({"username": username, "type": "web"})

        # Erp Login
        erp_user = db.admin_creds.find({"username": username, "type": "erp"})
        erp_users = db.admin_creds.count_documents({"username": username, "type": "erp"})

        if web_users != 0:
            for doc in web_user:
                db_password = doc["password"]
            if web_users == 0:
                error = 'Incorrect username.'
            elif password != db_password:
                error = 'Incorrect password.'

            if error is None:
                # session.clear()
                # session['user_id'] = user['id']
                return redirect(url_for('landing.web_index'))

        if erp_users != 0:
            for doc in erp_user:
                db_password = doc["password"]
            if erp_users == 0:
                error = 'Incorrect username.'
            elif password != db_password:
                error = 'Incorrect password.'

            if error is None:
                # session.clear()
                # session['user_id'] = user['id']
                return redirect(url_for('landing.erp_index'))

        flash(error)

    return render_template('auth/login.html')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password1 = request.form['password1']
        phone = request.form['phone']
        email = request.form['email']
        db = get_db()
        error = None
        web_users = db.users.count_documents({"username": username})

        if web_users == 0:
            db.users.insert_one({"username": username, "password": password1, "mail": email, "phone": phone})
            message = "SUCCESS"
            render_template("web")
        else:
            message = "USERNAME TAKEN"


        flash(error)

    return render_template('auth/register.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
