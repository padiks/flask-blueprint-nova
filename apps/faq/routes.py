# apps/faq/routes.py
from flask import Blueprint, render_template

# Define the blueprint
faq_bp = Blueprint(
    "faq",
    __name__,
    template_folder="templates",
)

# ---------------------------
# Page view
# ---------------------------
@faq_bp.route("/")
def view():
    """
    Render the FAQ page.
    """
    return render_template(
        "faq/view.html",
        title="FAQ",
    )
