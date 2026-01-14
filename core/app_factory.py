# core/app_factory.py
import os
from flask import Flask, redirect, url_for

from config import Config

# Import blueprints (feature-based modules)
from apps.home.routes import home_bp
from apps.about.routes import about_bp
from apps.pricing.routes import pricing_bp
from apps.works.routes import works_bp
from apps.services.routes import services_bp
from apps.testimonials.routes import testimonials_bp
from apps.faq.routes import faq_bp
from apps.contact.routes import contact_bp

# Import core infrastructure
from core.errors import register_error_handlers

# -----------------------------
# Project root directory
# -----------------------------
BASE_DIR = os.path.abspath(
    os.path.dirname(os.path.dirname(__file__))
)

# -----------------------------
# Application Factory
# -----------------------------
def create_app():
    # Create Flask app with explicit template and static paths
    app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, "templates"),
        static_folder=os.path.join(BASE_DIR, "static"),
    )

    # Load configuration from config.py
    app.config.from_object(Config)

    # -------------------------
    # Register blueprints
    # -------------------------
    app.register_blueprint(home_bp, url_prefix="/")
    app.register_blueprint(about_bp, url_prefix="/about")
    app.register_blueprint(pricing_bp, url_prefix="/pricing")
    app.register_blueprint(works_bp, url_prefix="/how-it-works")
    app.register_blueprint(services_bp, url_prefix="/services")
    app.register_blueprint(testimonials_bp, url_prefix="/testimonials")
    app.register_blueprint(faq_bp, url_prefix="/faq")
    app.register_blueprint(contact_bp, url_prefix="/contact")

    # -------------------------
    # Register global infrastructure
    # -------------------------
    register_error_handlers(app)
    # Middleware registration removed

    return app
