"""Script to seed database."""

import os
import json
from random import choice, randint

import crud
import model
import server

# os.system('dropdb ratings')
# More code will go here

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/plants.json') as f:
    plant_data = json.loads(f.read())

# TODO: lighting_file = open(lighting_conversion.txt)
# for line in file :
#     line = line.rstrip()
#     words = line.split('|')


# Create plants, store them in list so we can use them
# to create recommendations later


crud.create_lighting("Low Light")
crud.create_lighting("Medium Light")
crud.create_lighting("Bright Light")


crud.create_location("North Facing")
crud.create_location("East Facing")
crud.create_location("South Facing")
crud.create_location("West Facing")

plants_in_db = []
for plant in plant_data:
    # Get the name, description, lighting, location, and picture_path from the plant
    # dictionary.
    plant_name, plant_description, plant_lighting, plant_location, picture_path = (
                                    plant['plant_name'],
                                    plant['plant_description'],
                                    plant['plant_lighting'],
                                    plant['plant_location'],
                                    plant['picture_path'])
    
    light_id = crud.lighting_conversion(plant_lighting)
    location_id = crud.location_conversion(plant_location)

    db_plant = crud.create_plant(plant_name, plant_description, light_id, location_id, picture_path)

    plants_in_db.append(db_plant)


#Create 5 users
for n in range(5):
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(fname, lname, user_email, zip_code, password)

#  Create profiles for each user
    for n in range(5):
        random_plant = choice(plants_in_db)
        score = randint(1, 5)

        crud.create_plant(user, random_plant)

will make 2 plant requests