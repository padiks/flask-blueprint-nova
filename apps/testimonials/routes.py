# apps/testimonials/routes.py
from flask import Blueprint, render_template

# Define the blueprint
testimonials_bp = Blueprint(
    "testimonials",
    __name__,
    template_folder="templates",
)

# ---------------------------
# Page view
# ---------------------------
@testimonials_bp.route("/")
def view():
    """
    Render the Testimonials page.
    """
    return render_template(
        "testimonials/view.html",
        title="Testimonials",
    )
