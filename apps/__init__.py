# apps/__init__.py
from flask import Flask

def create_app():
    """
    Application factory function.
    Creates and configures the Flask app instance.
    Returns the Flask app object.
    """
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
	
    # Import blueprints (feature-based modules)
    from apps.home.routes import home_bp
    from apps.about.routes import about_bp
    from apps.pricing.routes import pricing_bp
    from apps.works.routes import works_bp
    from apps.services.routes import services_bp
    from apps.testimonials.routes import testimonials_bp
    from apps.faq.routes import faq_bp
    from apps.contact.routes import contact_bp	

    # Register blueprints
    app.register_blueprint(home_bp, url_prefix="/")
    app.register_blueprint(about_bp, url_prefix="/about")
    app.register_blueprint(pricing_bp, url_prefix="/pricing")
    app.register_blueprint(works_bp, url_prefix="/how-it-works")
    app.register_blueprint(services_bp, url_prefix="/services")
    app.register_blueprint(testimonials_bp, url_prefix="/testimonials")
    app.register_blueprint(faq_bp, url_prefix="/faq")
    app.register_blueprint(contact_bp, url_prefix="/contact")		
		

    # Add more blueprints as needed
    # from apps.<other_module>.routes import <other_module_bp>
    # app.register_blueprint(<other_module_bp>, url_prefix='/<other_module_prefix>')

    # Return the configured Flask app
    return app
