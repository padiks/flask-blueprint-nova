# apps/works/routes.py
from flask import Blueprint, render_template

# Define the blueprint
works_bp = Blueprint(
    "works",
    __name__,
    template_folder="templates",
)

# ---------------------------
# Page view
# ---------------------------
@works_bp.route("/")
def view():
    """
    Render the How It Works page.
    """
    return render_template(
        "works/view.html",
        title="How It Works",
    )
