from .base import db

import uuid
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime


class TestTable(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)
    name = db.Column(db.String())
    count = db.Column(db.Integer())
    number = db.Column(db.Integer())

    __tablename__ = 'test_table'

    def __init__(self, created, name, count):
        self.created = created
        self.name = name
        self.count = count
