from flask_combo_jsonapi import Api

from .tag import TagList, TagDetail

api = Api()

api.route(TagList, "tag_list", "/api/tags/")
api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/")
