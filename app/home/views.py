# app/home/views.py

from flask import render_template
from flask_login import login_required, current_user

from . import home

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/about')
def about():
    """
    Render the about template on the /about route
    """
    return render_template('home/about.html', title="About Us")

@home.route('/team')
def team():
    """
    Render the team template on the /team route
    """
    return render_template('home/team.html', title="Our Team")

@home.route('/services')
def services():
    """
    Render the services template on the /services route
    """
    return render_template('home/services.html', title="Our Services")

@home.route('/contact')
def contact():
    """
    Render the homepage template on the / route
    """
    return render_template('home/contact.html', title="Contact page")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

# add admin dashboard view
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")