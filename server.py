"""Server for plant recommendations app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
import random
import json
from jinja2 import StrictUndefined
# Might have to import sys and os

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

with open('data/facts.json') as f:
    plant_facts = json.loads(f.read())
options = []
for facts in plant_facts:
    fact = facts["plant_fact"]
    options.append(fact)


@app.route('/')
def homepage():
    """View homepage."""

    blurb = random.choice(options)
    return render_template('homepage.html', blurb=blurb)


@app.route('/plants')
def all_plants():
    """View all plants."""

    plants = crud.get_plants()
    return render_template('plant_options.html', plants=plants) 


@app.route('/plants/<plant_id>')
def show_plant(plant_id):
    """Show details on a specific plant."""

    plant = crud.get_plant_by_id(plant_id)
    if plant.light_id == 1:
        plant_lighting = "Low Light"
    if plant.light_id == 2:
        plant_lighting = "Medium Light"
    if plant.light_id == 3:
        plant_lighting = "Bright Light"

    if plant.location_id == 1:
        plant_location = "North Facing"
    if plant.location_id == 2:
        plant_location = "East Facing"
    if plant.location_id == 3:
        plant_location = "South Facing"
    if plant.location_id == 4:
        plant_location = "West Facing"
    return render_template('plant_details.html', plant=plant)


@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site."""

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)
    if user:
        if password == user.password:
            session['current_user'] = user.fname
            session['user_id'] = user.user_id
            flash('Success! Happy plantin!')
            return redirect('/user-home')
        elif password != user.password:
            flash('Incorrect password. Try again.')
            return redirect('/login')
    else:
        flash('Email account does not exist. Please try again.')
        return redirect('/login')


@app.route("/logout")
def logout():
    """Logout user."""

    session.clear()
    return redirect("/")


@app.route('/user-home')
def show_user_home():
    """Show user homepage."""

    return render_template("user_home.html")


@app.route('/register-user')
def show_registration():
    """Show new user form."""

    return render_template("new_user_form.html")


@app.route('/register-user', methods=['POST'])
def register_user():
    """Create a new user."""

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('user_email')
    zip_code = request.form.get('zip_code')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash('That email already exists. Try again.')
        return redirect('/register-user')
    else:
        user = crud.create_user(fname, lname, email, zip_code, password)
        flash('Account created! Please log in.')
    return render_template('login.html', user=user)


@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details on a specific user."""

    user = crud.get_user_by_id(user_id)
    return render_template('user_details.html', user=user)


@app.route('/plant-form')
def show_plant_form():
    """Show plant form."""

    return render_template('plant_form.html')


@app.route('/plant-recommends') 
def show_plant_recommends():
    """Show plant recommendations."""

    lighting = request.args.get("lighting")
    location = request.args.get("location")
    plant_recommends = []
    light_recommends = crud.get_plant_by_lighting(lighting)
    location_recommends = crud.get_plant_by_location(location)
    for plant in light_recommends:
        if plant in location_recommends:
            plant_recommends.append(plant)
    return render_template('plant_recommends.html', plant_recommends=plant_recommends) 


@app.route('/profile')
def show_plant_profile():
    """Show plant greenhouse."""

    user_id = session['user_id']
    plants_added = crud.get_profile_by_user_id(user_id)
    if plants_added == None:
        flash('Your greenhouse is empty! How bout some new guests?')
        return redirect ('/plant-form')
    else:
        return render_template('plant_profile.html', plants_added=plants_added)


@app.route('/profile', methods=['POST'])
def create_plant_profile():
    """Create greenhouse for a specific user and add plant."""

    if session.get('user_id'):
        user_id = session['user_id']
        plant_id= request.form['plant-id']
        current_plant_profile = crud.create_plant_profile(user_id, plant_id)
        plants_added = crud.get_profile_by_user_id(user_id)
        return render_template('plant_profile.html', plants_added=plants_added)
    else:
        flash(f'Your account was not found, please login or create an account')
        session['name'] = 'no-account-found-please-create-account'
        return redirect('/login')


@app.route('/remove-plant', methods=['POST'])
def remove_plant_():
    """Remove plant from greenhouse."""
    
    user_id = session['user_id']
    plant_profile_id= request.form['plant-id']
    current_plant_profile = crud.remove_plant(plant_profile_id)
    plants_added = crud.get_profile_by_user_id(user_id)
    return render_template('plant_profile.html', plants_added=plants_added)


@app.route('/map')
def show_map():
    """Render map to page."""

    return render_template('map.html', map=map)

# @app.route("/update-user", methods=["POST"])
# def update_user_fname():
#     """Allow user to update their own fname from their profile screen."""
    
#     existing_user = crud.get_user_by_email(session['email']) ### USES THE SESSION INFO INSTEAD OF A A HIDDEN INPUT ###
#     fname = request.form.get('name-input')

#     crud.update_user_fname(existing_user.id, fname)

#     session['name'] = fname  ### THEN ALSO OVERWIRE/UPDATE/RESET THE SESSION INFO FOR THE THING THAT YOU'RE ALSO SETTING IN THE DB##
#     flash(f"Your name has been successfully updated to: ''{fname}''")

#     return redirect('/profile')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)