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
            return redirect('/plant-form')
        elif password != user.password:
            flash('Incorrect password. Try again.')
            return redirect('/login')
    else:
        flash('Email account does not exist. Please try again.')
        return redirect('/login')


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
    print(location)
    print(lighting)
    # show_plant(plant_id)
    plant_recommends = []
    light_recommends = crud.get_plant_by_lighting(lighting)
    location_recommends = crud.get_plant_by_location(location)
    for plant in light_recommends:
        if plant in location_recommends:
            plant_recommends.append(plant)

    print(plant_recommends)
    

    return render_template('plant_recommends.html', plant_recommends=plant_recommends) #KEEP AN EYE ON THIS AND ASK FOR LUCIA IF YOU GET A PROBLEM

@app.route('/profile', methods=['POST'])
def show_plant_profile():
    """Create profile for a specific user and add plant."""
    # user_id = request.form['user-id']
    # print(f"***************{user_id}********")
    # user = crud.get_user_by_id(1)
    user_id = session['user_id']

    plant_id= request.form['plant-id']
    # print(f"*******{plant_id}*************")
    # plant = crud.get_plant_by_id(plant_id)
    # print(f'********{plant}********')
    plant_profile = crud.create_plant_profile(user_id, plant_id)
    

    return render_template('plant_profile.html', plant_profile=plant_profile)

# @app.route('/profiles/<plant_profile_id>')
# def plant_profile():
#     """Show profile for a specific user."""

#     profile = crud.get_profile_by_id(plant_profile_id)
#     print(profile)

    return render_template('plant_profile.html', profile=profile)
# "/add-to-profile" method="POST">
#   <p>Add to profile?</p>
#   <input type="submit">

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)





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

#     @app.route("/add_to_cart/<melon_id>")
# def add_to_cart(melon_id):
#     """Add a melon to cart and redirect to shopping cart page.

#     When a melon is added to the cart, redirect browser to the shopping cart
#     page and display a confirmation message: 'Melon successfully added to
#     cart'."""

#     # Check if we have a cart in the session and if not, add one
#     # Also, bind the cart to the name 'cart' for easy reference below
#     if 'cart' in session:
#         cart = session['cart']
#     else:
#         cart = session['cart'] = {}

    # We could also do this with setdefault:
    # cart = session.setdefault("cart", {})

    # Add melon to cart - either increment the count (if melon already in cart)
    # or add to cart with a count of 1
    # cart[melon_id] = cart.get(melon_id, 0) + 1

    # # Print cart to the terminal for testing purposes
    # # print("cart:")
    # # print(cart)

    # # Show user success message on next page load
    # flash("Melon successfully added to cart.")


@app.route("/cart")
def show_shopping_cart():
    """Display content of shopping cart."""

    # Keep track of the total cost of the order
    order_total = 0

    # Create a list to hold Melon objects corresponding to the melon_id's in
    # the cart
    cart_melons = []

    # Get the cart dictionary out of the session (or an empty one if none
    # exists yet)
    cart = session.get("cart", {})

    # Loop over the cart dictionary
    for melon_id, quantity in cart.items():
        # Retrieve the Melon object corresponding to this id
        melon = melons.get_by_id(melon_id)

        # Calculate the total cost for this type of melon and add it to the
        # overall total for the order
        total_cost = quantity * melon.price
        order_total += total_cost

        # Add the quantity and total cost as attributes on the Melon object
        melon.quantity = quantity
        melon.total_cost = total_cost

        # Add the Melon object to our list
        cart_melons.append(melon)

    # Pass the list of Melon objects and the order total to our cart template

    return render_template("cart.html",
                           cart=cart_melons,
                           order_total=order_total)

# @app.route('/users')
# def all_users():
#     """View all users."""

#     users = crud.get_users()

#     return render_template('all_users.html', users=users)

# @app.route('/create-account')
# def create_account():
#     """Create an account."""

#     user = crud.create_user()

#     return render_template('all_users.html', user=user)