"""Application factory for Casa Nativa."""

from flask import Flask

from config import get_config


def create_app(config_name: str | None = None) -> Flask:
    """Create and configure the Flask application instance."""
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))

    if app.config["ENVIRONMENT"] == "production" and not app.config.get("SECRET_KEY"):
        raise RuntimeError("SECRET_KEY must be configured in production.")

    from app.routes.main import main_bp

    app.register_blueprint(main_bp)

    return app
