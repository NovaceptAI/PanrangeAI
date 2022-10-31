import os
from flask import Flask, jsonify
# from flask.ext.session import Session
from .models import auth, landing_pages, web_app
from .models.erp import inventory_management, finance, hrm, crm, marketing, company, automation, s_s, t_p, \
    collaboration, more
from .models.web_app import shop
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
    jwt = JWTManager(app)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Add Blueprints
    app = add_blueprints(app)

    return app


def add_blueprints(app):
    # Add Blueprints
    app.register_blueprint(auth.bp)
    app.register_blueprint(landing_pages.bp)
    app.register_blueprint(inventory_management.bp)
    app.register_blueprint(shop.bp)
    app.register_blueprint(finance.bp)
    app.register_blueprint(hrm.bp)
    app.register_blueprint(crm.bp)
    app.register_blueprint(marketing.bp)
    app.register_blueprint(company.bp)
    app.register_blueprint(automation.bp)
    app.register_blueprint(s_s.bp)
    app.register_blueprint(t_p.bp)
    app.register_blueprint(collaboration.bp)
    app.register_blueprint(more.bp)

    return app


app = create_app()


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
