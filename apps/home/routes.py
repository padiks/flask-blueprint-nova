# apps/home/routes.py
from flask import Blueprint, render_template

# Define the blueprint
home_bp = Blueprint(
    "home",
    __name__,
    template_folder="templates",
)

# ---------------------------
# Page view
# ---------------------------
@home_bp.route("/")
def view():
    """
    Render the Home page.
    """
    return render_template(
        "home/view.html",
        title="Home",
    )
