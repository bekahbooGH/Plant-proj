# """CRUD operations."""

from model import db, User, Plant, Profile, Lighting, Location, connect_to_db


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



def get_users():
    """returns all users"""

    return User.query.all()


def get_user_by_id(user_id):

    return User.query.filter(User.user_id == user_id).first()

def get_user_by_email(user_email):
    """Return a user by email."""

    return User.query.filter(User.user_email == user_email).first()


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

def lighting_conversion(plant_lighting):
    """Take in lighting name and return light_id."""
    if plant_lighting == "Low Light":
        light_id = 1
    elif plant_lighting == "Medium Light":
        light_id = 2
    elif plant_lighting == "Bright Light":
        light_id = 3

    return light_id


def location_conversion(plant_location):
    """Take in location name and return location_id."""
    if plant_location == "North Facing":
        location_id = 1
    elif plant_location == "East Facing":
        location_id = 2
    elif plant_location == "South Facing":
        location_id = 3
    elif plant_location == "West Facing":
        location_id = 4 

    return location_id


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
    """returns all plants to page"""

    all_plants = Plant.query.all()
    # for plant in all_plants:


    #     return plant
    return all_plants
 


def get_plant_by_id(plant_id):

    this_plant =  Plant.query.get(plant_id)

    return this_plant

def get_plant_by_lighting(light_id):
    """Return a plant by lighting id."""

    return Plant.query.filter(Plant.light_id == light_id).all()

def get_plant_by_location(location_id):
    """Return a plant by location id."""

    return Plant.query.filter(Plant.location_id == location_id).all()




def create_plant_profile(user_id, plant_id):
    """Create and return a new plant profile for user."""

    plant_profile = Profile(user_id=user_id, plant_id=plant_id)

    db.session.add(plant_profile)
    db.session.commit()

    return plant_profile

def get_profile_by_user_id(user_id):

    profile =  Profile.query.filter(Profile.user_id == user_id).all()
    return profile

def get_profile_by_id(plant_profile_id):

    profile =  Profile.query.get(plant_profile_id)
    return profile
    
def remove_plant(plant_profile_id):
    """Remove a plant from profile for user."""
    profile =  Profile.query.get(plant_profile_id)

    db.session.delete(profile)
    db.session.commit()
    

if __name__ == '__main__':
    from server import app
    connect_to_db(app)