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

# Create plants, store them in list so we can use them
# to create fake recommendations later
plants_in_db = []
for plant in plant_data:
    # TODO: get the name, description, lighting, location, and picture_path from the movie
    # dictionary.
    plant_name, plant_overview, plant_lighting, plant_description, picture_path = (
                                    plant['plant_name'],
                                    plant['plant_description'],
                                    plant['plant_lighting']
                                    plant['plant_location']
                                    plant['picture_path'])
    
    

    db_plant = crud.create_plant(title,
                             overview,
                             release_date,
                             poster_path)

    plants_in_db.append(db_plant)
    # TODO: create a plant here and append it to plants_in_db

# Create 10 users; each user will make 1 plant request
for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = crud.create_user(fname, lname, user_email, zip_code, password)

    # for n in range(10):
    #     random_plant = choice(plants_in_db)
    #     score = randint(1, 5)

    #     crud.create_plant(user, random_plant)