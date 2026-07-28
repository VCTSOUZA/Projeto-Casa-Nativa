"""Main site routes."""

from flask import Blueprint, render_template


main_bp = Blueprint("main", __name__)


@main_bp.get("/")
def home():
    """Render the initial Casa Nativa page."""
    collections = (
        {"name": "Sala", "description": "Conforto para os encontros que ficam."},
        {"name": "Quarto", "description": "Pausas tranquilas para chamar de suas."},
        {"name": "Cozinha", "description": "Rituais simples, todos os dias."},
        {"name": "Decoração", "description": "Detalhes que contam histórias."},
    )
    products = (
        {"name": "Vaso Terracota", "category": "Decoração", "price": "R$ 189,00", "badge": "Novo"},
        {"name": "Cesto de Fibra Natural", "category": "Organização", "price": "R$ 249,00", "badge": None},
        {"name": "Luminária de Mesa", "category": "Iluminação", "price": "R$ 329,00", "badge": None},
        {"name": "Manta de Linho", "category": "Têxteis", "price": "R$ 279,00", "badge": "Destaque"},
    )
    return render_template("home.html", collections=collections, products=products)
