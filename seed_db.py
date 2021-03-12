"""Script to seed database."""

import os
import json
from random import choice, randint
import crud
import model
import server


os.system('dropdb plants')
os.system('createdb plants')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/plants3.json') as f:
    plant_data = json.loads(f.read())

# Create locations and lighting conditions, store them in list so we can use them
# to create plants later

crud.create_lighting("Low Light")
crud.create_lighting("Medium Light")
crud.create_lighting("Bright Light")

crud.create_location("North Facing")
crud.create_location("East Facing")
crud.create_location("South Facing")
crud.create_location("West Facing")

# Create plants, store them in list so we can use them
# to create recommendations later

plants_in_db = []
for plant in plant_data:
    # Get the name, description, lighting, location, and picture_path from the plant
    # dictionary.
    plant_name, plant_description, plant_lighting, plant_location, pic_src = (
                                    plant['plant_name'],
                                    plant['plant_description'],
                                    plant['plant_lighting'],
                                    plant['plant_location'],
                                    plant['pic_src'])
    light_id = crud.lighting_conversion(plant_lighting)
    location_id = crud.location_conversion(plant_location)
    db_plant = crud.create_plant(plant_name, plant_description, light_id, location_id, pic_src)
    plants_in_db.append(db_plant)


# Create greenhouse profiles for each user
users_in_db = crud.User.query.all()
profiles_in_db = []
for user in users_in_db:
    profile = crud.create_plant_profile(user_id, plant_id)
    profiles_in_db.append(plant_profile)