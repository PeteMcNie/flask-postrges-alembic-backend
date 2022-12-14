import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID

from .base import db


class ExampleTable(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    name = db.Column(db.String())
    count = db.Column(db.Integer())
    number = db.Column(db.Integer())

    __tablename__ = "example_table"

    def __init__(self, created, name, count):
        self.created = created
        self.name = name
        self.count = count
