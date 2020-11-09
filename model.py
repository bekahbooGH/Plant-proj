"""Models for plant recommendations app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    user_email = db.Column(db.String, unique=True)
    zip_code = db.Column(db.Integer)
    password = db.Column(db.String)

    profile = db.relationship('Profile')

    # users = a list of User objects

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.user_email}>'

class Profile(db.Model):
    """A user's plant profile"""

    __tablename__ = 'profiles'

    
    plant_profile_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(users.user_id))
    plant_id = db.Column(db.Integer, db.ForeignKey(plants.plant_id))
    
    user = db.relationship('User')
    plant = db.relationship('Plant')

    # profiles = a list of user plant Profile objects

    def __repr__(self):
        return f'<Profile plant_profile_id={self.plant_profile_id} user_id={self.user_id}>'
    


class Plant(db.Model):
    """A plant"""

    __tablename__ = 'plants'

    plant_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    plant_name = db.Column(db.String)
    plant_description = db.Column(db.Text)
    light_id = db.Column(db.Integer, db.ForeignKey(lightings.light_id))
    location_id = db.Column(db.Integer, db.ForeignKey(locations.location_id))
    picture_path = db.Column(db.String)


    lighting = db.relationship('Lighting')
    location = db.relationship('Location')
    profile = db.relationship('Profile')


    # plants = a list of Plant objects

    def __repr__(self):
        return f'<Plant plant_id={self.plant_id} plant_name={self.plant_name}>'


class Lighting(db.Model):
    """A plant light condition"""

    __tablename__ = 'lightings'

    light_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    plant_lighting = db.Column(db.String)
   

    plant = db.relationship('Plant')

    # lightings = a list of Lighting objects

    def __repr__(self):
        return f'<Lighting light_id={self.light_id} lighting_type={self.plant_lighting}>'



class Location(db.Model):
    """A plant location"""

    __tablename__ = 'locations'

    location_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    plant_location = db.Column(db.String)

    plant = db.relationship('Plant')

    
    # locations = a list of Location objects

    def __repr__(self):
        return f'<Location location_id={self.location_id} location_type={self.plant_location}>'


def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)