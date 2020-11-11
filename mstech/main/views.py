from . import bp


@bp.route("/")
@bp.route("/index")
def index():
    return "Welcome to MsTech Club"
