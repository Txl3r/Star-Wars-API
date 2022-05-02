from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)

    def __repr__(self):
        return '<People %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.Integer(50), unique=True, nullable=False)
    gravity = db.Column(db.Integer(50), unique=True, nullable=False)
    population = db.Column(db.Integer(50), unique=True, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.planet_name,
            "climate": self.climate,
            "gravity": self.gravity,
            "population": self.population,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.Integer(50), unique=True, nullable=False)
    age = db.Column(db.Integer(50), unique=True, nullable=False)
    hair_color = db.Column(db.String(60), unique=True, nullable=False)
    eye_color = db.Column(db.String(60), unique=True, nullable=False)
    planet = db.Column(db.String(60), unique=True, nullable=False)

    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.character_name,
            "height": self.height,
            "age": self.age,
            "hair color": self.hair_color,
            "eye color": self.eye_color,
            "planet": self.planet_name,
            # do not serialize the password, its a security breach
        }