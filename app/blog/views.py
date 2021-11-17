# app/blog/views.py

from flask import render_template
from flask_login import login_required

from . import blog

@blog.route('/blog')
def blogpage():
    """
    Render the blogpage template on the / route
    """
    return render_template('blog/blog.html', title="Blog")

@blog.route('/page')
def blogsinglepage():
    """
    Render the blogpage template on the /page route
    """
    return render_template('blog/single.html', title="Blog Page")