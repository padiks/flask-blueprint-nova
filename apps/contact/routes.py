# apps/contact/routes.py
from flask import Blueprint, render_template

# Define the blueprint
contact_bp = Blueprint(
    "contact",
    __name__,
    template_folder="templates",
)

# ---------------------------
# Page view
# ---------------------------
@contact_bp.route("/")
def view():
    """
    Render the Contact page.
    """
    return render_template(
        "contact/view.html",
        title="Contact",
    )
