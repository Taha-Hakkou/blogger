#!/usr/bin/python3
""" error views """
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, expose, has_access
from . import appbuilder, db


@appbuilder.app.errorhandler(404)
def error_404(error):
    """ 404 error handler """
    return render_template("errors/404.html"), 404


@appbuilder.app.errorhandler(403)
def error_403(error):
    """ 403 error handler """
    return render_template('errors/403.html'), 403


@appbuilder.app.errorhandler(500)
def error_500(error):
    """ 500 error handler """
    return render_template('errors/500.html'), 500