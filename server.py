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

    # if light_id == "1":
    #     plant_lighting = "Low Light"
    # if light_id == "2":
    #     plant_lighting = "Medium Light"
    # if light_id == "3":
    #     plant_lighting = "Bright Light"

    # if location_id == "1":
    #     plant_location = "North Facing"
    # if location_id == "2":
    #     plant_location = "East Facing"
    # if location_id == "3":
    #     plant_location = "South Facing"
    # if location_id == "4":
    #     plant_location = "West Facing"

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

@app.route("/add_to_cart/<melon_id>")
def add_to_cart(melon_id):
    """Add a melon to cart and redirect to shopping cart page.

    When a melon is added to the cart, redirect browser to the shopping cart
    page and display a confirmation message: 'Melon successfully added to
    cart'."""

    # Check if we have a cart in the session and if not, add one
    # Also, bind the cart to the name 'cart' for easy reference below
    if 'cart' in session:
        cart = session['cart']
    else:
        cart = session['cart'] = {}

    # We could also do this with setdefault:
    # cart = session.setdefault("cart", {})

    # Add melon to cart - either increment the count (if melon already in cart)
    # or add to cart with a count of 1
    cart[melon_id] = cart.get(melon_id, 0) + 1

    # Print cart to the terminal for testing purposes
    # print("cart:")
    # print(cart)

    # Show user success message on next page load
    flash("Melon successfully added to cart.")

@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")

@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site."""

     # The logic here should be something like:
    #
    # - get user-provided name and password from request.form
    # - use customers.get_by_email() to retrieve corresponding Customer
    #   object (if any)
    # - if a Customer with that email was found, check the provided password
    #   against the stored one
    # - if they match, store the user's email in the session, flash a success
    #   message and redirect the user to the "/melons" route
    # - if they don't, flash a failure message and redirect back to "/login"
    # - do the same if a Customer with that email doesn't exist


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

@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(email, password)
        flash('Account created! Please log in.')

    return redirect('/')

@app.route("/login/plant_form")
def show_plant_form():
    """Show plant form."""

    return render_template("plant_form.html")

@app.route('/profiles/<plant_profile_id>')
def show_plant_profile(plant_profile_id):
    """Show profile for a specific user."""

    profile = crud.get_profile_by_id(plant_profile_id)

    return render_template('plant_profile.html', profile=profile)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
