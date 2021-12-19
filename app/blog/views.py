# app/blog/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from flask_sqlalchemy import SQLAlchemy


from . import blog
from .forms import ArticleForm, CartegoryForm
from .. import db 
from ..models import Article, Cartegory

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

@blog.route('/list_articles')
@login_required
def list_articles():
    """
    List articles from database
    """

    articles = Article.query.all()
    return render_template('blog/articles.html', title="Articles", articles=articles)

@blog.route('/add_article', methods=['GET', 'POST'])
@login_required
def add_article():
    """
    Add article to database
    """

    add_article = True
    
    form = ArticleForm()
    if form.validate_on_submit():
        article = Article(title=form.title.data,
                            author=form.author.data,
                            body=form.body.data,
                            tags=form.tags.data,
                            draft=form.draft.data)
        try:
            #add article to the database
            db.session.add(article)
            db.session.commit()
            flash('You have successfully added a new article')
        except:
            #in case article submissin fails
            flash('Error: An error occured submitting your article.')

        # redirect to articles page
        return redirect(url_for('blog.list_articles')) 

    return render_template('blog/article.html', action="Add",add_article=add_article, form=form, title="New Article")


@blog.route('/articles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_article(id):
    """
    Edit an article
    """
    

    add_article = False

    article = Article.query.get_or_404(id)
    form = ArticleForm(obj=article)
    if form.validate_on_submit():
        article.title=form.title.data,
        article.author=form.author.data,
        article.body=form.body.data,
        article.tags=form.tags.data,
        article.draft=form.draft.data

        
        db.session.commit()
        flash('You have successfully edited article.')

        # redirect to the articles page
        return redirect(url_for('blog.list_articles'))

    form.title.data=article.title
    form.author.data=article.author
    form.body.data=article.body
    form.tags.data=article.tags
    form.draft.data=article.draft
    return render_template('blog/article.html', action="Edit", add_article=add_article,
                           form=form, title="Edit Article")

@blog.route('/articles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_article(id):
    """
    Delete an article from the database 
    """

    article = Article.query.get_or_404(id)

    db.session.delete(article)
    db.session.commit()
    flash('You have successfully deleted the article')

    # redirect to the articles page
    return redirect(url_for('blog.list_articles'))
    

    return render_template(title="Delete Article")