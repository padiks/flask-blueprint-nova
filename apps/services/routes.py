# apps/services/routes.py
from flask import Blueprint, render_template

# Define the blueprint
services_bp = Blueprint(
    "services",
    __name__,
    template_folder="templates",
)

# ---------------------------
# Page view
# ---------------------------
@services_bp.route("/")
def view():
    """
    Render the Services page.
    """
    return render_template(
        "services/view.html",
        title="Services",
    )
