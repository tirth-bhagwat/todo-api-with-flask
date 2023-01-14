import uuid
from api import db
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID, VARCHAR


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(
        UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    username = db.Column(VARCHAR(80), unique=True, nullable=False)
    password = db.Column(VARCHAR(80), nullable=False)

    def json(self):
        return {
            "username": self.username,
            "password": self.password,
        }

    def __repr__(self):
        return f"User('{self.username}')"
