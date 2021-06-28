from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship

from blog.instruments import db


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, default="", server_default="")
    articles = relationship(
        "Article",
        secondary=article_tag_association_table,
        back_populates="tags",
    )


article_tag_association_table = Table(
    "article_tag_association",
    db.metadata,
    db.Column("article_id", db.Integer, ForeignKey("article.id"), nullable=False),
    db.Column("tag_id", db.Integer, ForeignKey("tag.id"), nullable=False),
)
