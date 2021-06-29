from sqlalchemy.orm import relationship

from blog.instruments import db
from blog.models.article_tag import article_tag_association_table


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, default='', server_default='')

    articles = relationship('Article', secondary=article_tag_association_table, back_populates='tags')
