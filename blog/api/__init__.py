from flask_combo_jsonapi import Api

from .article import ArticleList, ArticleDetail
from .author import AuthorList, AuthorDetail
from .tag import TagList, TagDetail
from .user import UserList, UserDetail

api = Api()

api.route(TagList, "tag_list", "/api/tags/", tag="Tag")
api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/", tag="Tag")
api.route(UserList, "user_list", "/api/users/", tag="User")
api.route(UserDetail, "user_detail", "/api/users/<int:id>/", tag="User")
api.route(AuthorList, "author_list", "/api/authors/", tag="Author")
api.route(AuthorDetail, "author_detail", "/api/authors/<int:id>/", tag="Author")
api.route(ArticleList, "article_list", "/api/articles/", tag="Article")
api.route(ArticleDetail, "article_detail", "/api/articles/<int:id>/", tag="Article")
