# app/blog/views.py

from flask import render_template
from flask_login import login_required

from . import blog

@blog.route('/')
def blogpage():
    """
    Render the blogpage template on the / route
    """
    return render_template('blog/blog.html', title="Blog")