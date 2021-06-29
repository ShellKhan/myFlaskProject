from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.instruments import db
from blog.forms import CreateArticleForm
from blog.models import Author, Article, Tag

article = Blueprint(
    name='article',
    import_name=__name__,
    url_prefix='/articles',
    static_folder='../static',
)


@article.route('/', methods=['GET'])
def article_list():
    articles = Article.query.all()
    return render_template(
        'articles/list.html',
        articles=articles,
    )


@article.route('/tags/<int:tag_id>/', methods=['GET'])
def article_tag_list(tag_id):
    tag = Tag.query.filter_by(id=tag_id).options(joinedload(Tag.articles)).one_or_none()
    return render_template(
        'articles/list.html',
        articles=tag.articles,
        tag=tag
    )


@article.route('/<int:article_id>/', methods=['GET'])
def article_detail(article_id):
    _article = Article.query.filter_by(id=article_id).options(joinedload(Article.tags)).one_or_none()
    if _article is None:
        raise NotFound
    return render_template(
        'articles/details.html',
        article=_article,
    )


@article.route('/create/', methods=['GET', 'POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]

    if request.method == "POST" and form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), text=form.text.data)

        if current_user.author:
            _article.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id = author.id

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('article.article_detail', article_id=_article.id))

    return render_template('articles/create.html', form=form)
