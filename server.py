"""Server for plant recommendations app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined





@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/plants')
def all_plants():
    """View all plants."""

    plants = crud.get_plants()

    return render_template('plant_options.html', plants=plants) 

@app.route('/plants/<plant_id>')
def show_plant(plant_id):
    """Show details on a specific plant."""

    plant = crud.get_plant_by_id(plant_id)

    return render_template('plant_details.html', plant=plant)

@app.route('/users')
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template('all_users.html', users=users)


@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details on a specific user."""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
