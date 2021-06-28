from sqlalchemy import Table, ForeignKey

from blog.instruments import db

article_tag_association_table = Table(
    "article_tag_association",
    db.metadata,
    db.Column("article_id", db.Integer, ForeignKey("article.id"), nullable=False),
    db.Column("tag_id", db.Integer, ForeignKey("tag.id"), nullable=False),
)