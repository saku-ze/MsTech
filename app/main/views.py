from . import bp


@bp.route("/")
@bp.route("/index")
def index():
    return "Hi, Nice to meet you"
