from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String, unique=True)

    def __repr__(self):
        return f'<User id={self.id} name={self.name}>'


class Reservation(db.Model):
    """Table to store reservations."""

    __tablename__ = 'reservations'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    date = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)

    user = db.relationship("User", backref="reservations")

    def __repr__(self):
        return f'<Reservation id={self.id} user_id={self.user_id} time={self.time} '


def connect_to_db(app, db_uri="postgresql:///reservations", echo=False):
    """Connect the database to our Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = echo
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

    print("Connected to the db!")


if __name__ == "__main__":
    from app import app
    connect_to_db(app)