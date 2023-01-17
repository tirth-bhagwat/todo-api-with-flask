from api import db
from sqlalchemy.dialects.postgresql import UUID, VARCHAR, INTEGER
import uuid


class Todo(db.Model):
    __tablename__ = "todos"
    id: uuid = db.Column(
        UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    title: str = db.Column(VARCHAR(50), nullable=False)
    description: str = db.Column(VARCHAR(200), nullable=False)
    priority: int = db.Column(INTEGER, nullable=False)
    status: str = db.Column(VARCHAR(10), nullable=False)

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
        }

    def __repr__(self):
        return f"Todo('{self.title}')"
