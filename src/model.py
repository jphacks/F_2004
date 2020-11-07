from . import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.functions import current_timestamp

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    is_watch = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(
        db.TIMESTAMP,
        server_default=current_timestamp(),
        default=current_timestamp(),
        nullable=False
    )

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            is_watch=self.is_watch,
            created_at=self.created_at
        )

    def __repr__(self):
        return f'<User {self.id}:{self.name},{self.created_at}>'


class ConcentrationValue(db.Model):
    __tablename__ = "concentration_values"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True, nullable=False)
    concentration_value = db.Column(db.SMALLINT, nullable=False)
    is_sitting = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(
        db.TIMESTAMP,
        server_default=current_timestamp(),
        default=current_timestamp(),
        primary_key=True,
        nullable=False
    )

    def to_dict(self):
        return dict(
            user_id=self.user_id,
            concentration_value=self.concentration_value,
            is_sitting=self.is_sitting,
            created_at=self.created_at
        )

    def __repr__(self):
        return f'<ConcentrationValue {self.user_id}({self.created_at}):{self.concentration_value},{self.is_sitting}>'
