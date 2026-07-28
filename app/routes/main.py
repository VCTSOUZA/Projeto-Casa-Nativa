"""Main site routes."""

from flask import Blueprint, render_template


main_bp = Blueprint("main", __name__)


@main_bp.get("/")
def home():
    """Render the initial Casa Nativa page."""
    return render_template("home.html")
