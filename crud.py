# """CRUD operations."""

from model import db, User, Plant, Profile, Lighting, Location, connect_to_db

# Functions start here!!!!!

def create_user(fname, lname, user_email, zip_code, password):
    """Create and return a new user."""

    user = User(fname=fname, 
                lname=lname, 
                user_email=user_email, 
                zip_code=zip_code, 
                password=password)

    db.session.add(user)
    db.session.commit()

    return user



# def get_users():
#     """returns all users"""

#     return User.query.all()


# def get_user_by_id(user_id):

#     return User.query.get(user_id)


def create_plant(plant_name, plant_description, light_id, location_id, picture_path):
    """Create and return a new plant."""

    plant = Plant(plant_name=plant_name,
                plant_description=plant_description,
                light_id=light_id,
                location_id=location_id,
                picture_path=picture_path)

    db.session.add(plant)
    db.session.commit()

    return plant


def get_plants():
    """returns all plants"""

    return Plant.query.all()


def get_plant_by_id(plant_id):

    return Plant.query.get(plant_id)


def create_lighting(plant_lighting):
    """Create a lighting type for plants"""
    
    lighting = Lighting(plant_lighting=plant_lighting)

    db.session.add(lighting)
    db.session.commit()

    return lighting

def create_location(plant_location):
    """Create a location type for plants"""
    
    location = Location(plant_location=plant_location)

    db.session.add(location)
    db.session.commit()

    return location
    


if __name__ == '__main__':
    from server import app
    connect_to_db(app)