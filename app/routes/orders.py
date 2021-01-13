from flask import Blueprint
from flask_login import login_required
from ..forms import LoginForm

bp = Blueprint("orders", __name__, url_prefix="")

@bp.route("/")
@login_required
def index():
    return "Order Up!"
