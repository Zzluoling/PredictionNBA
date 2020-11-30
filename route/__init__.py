from .index import main
from .log import log


def init_app(app):
    app.register_blueprint(main)
    app.register_blueprint(log)
