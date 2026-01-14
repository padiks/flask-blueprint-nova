# apps/about/routes.py
from flask import Blueprint, render_template

# Define the blueprint
about_bp = Blueprint(
    "about",
    __name__,
    template_folder="templates",
)

# ---------------------------
# Page view
# ---------------------------
@about_bp.route("/")
def view():
    """
    Render the About page.
    """
    return render_template(
        "about/view.html",
        title="About",
    )
