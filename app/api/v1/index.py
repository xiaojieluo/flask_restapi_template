from app.libs.error_code import Success, ParameterException
from app.libs.redprint import Redprint
from app.models.user import User
from flask import Blueprint

api = Redprint('/')

@api.route("/")
def index():
    return Success()
