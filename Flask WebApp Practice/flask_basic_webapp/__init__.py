from flask import Flask


def create_app(config: dict | None = None) -> Flask:
    """Application factory for the Flask app.

    Accepts an optional config dictionary to make testing and reuse easier.
    """
    app = Flask(__name__)
    if config:
        app.config.update(config)

    from .routes import bp
    app.register_blueprint(bp)

    return app
