from flask import Blueprint, render_template

from blog.models.author import Author

author = Blueprint(
    name='author',
    import_name=__name__,
    url_prefix='/author',
    static_folder='../static',
)


@author.route('/')
def author_list():
    authors = Author.query.all()
    return render_template(
        'authors/list.html',
        authors=authors,
    )
