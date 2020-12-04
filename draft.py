

#*############################################################################*#
#*#                             SERVER.PY                                    #*#
#*############################################################################*#
# so, like, in your routes on youre ***server.py*** file... you can use things like this:

# if login_user:
#   return render_template('profile.html', user=login_user)                 #preferences=user_prefs

# else:
#   flash(f'Your account was not found, please login or create an account')
#   session['name'] = 'no-account-found-please-create-account'
#   return redirect('/')


@app.route("/updateuserfname", methods=["POST"])
  def update_user_fname():
      """Allow user to update their own fname from their profile screen."""
      
      existing_user = crud.get_user_by_email(session['email']) ### USES THE SESSION INFO INSTEAD OF A A HIDDEN INPUT ###
      fname = request.form.get('name-input')
  
      crud.update_user_fname(existing_user.id, fname)
  
      session['name'] = fname  ### THEN ALSO OVERWIRE/UPDATE/RESET THE SESSION INFO FOR THE THING THAT YOU'RE ALSO SETTING IN THE DB##
      flash(f"Your name has been successfully updated to: ''{fname}''")
  
      return redirect('/profile')



  #*############################################################################*#
  #*#                             .HTML FILES                                  #*#
  #*############################################################################*#
and on the ***HTML page(s)*** you can use "if" statements in jinja formatting type stuff... and you can nest your logic

WHICH GENERALLY GOES SOMETHING LOGICAL LIKE A FLOWCHART:
if highlevel thing is true/false:  #like, logged_in == True
  #choose your own adventure 

    if granular thing blah blah:  #and they already have a plant.... like... add a query here?  to check the 
      #then display something unique to that situation    #then display button that allows increment

    elif other granular thing:  #otherwise they don't already have the plant
       #then other stuff instead   #then display a different button that allows to add only

else:  #like logged_in is not defined (never logged in to begin with), or logged_in == False (logged out)
  simplest "no" answer


</li>{% if session['current_user'] %}
        <li class="nav-item">
          <a class="nav-link" href="/logout">Logout</a>
        </li>
        {% else %}
{% endif %}



WHICH ACTUALLY LOOKS MORE LIKE GARBAGE:
  <div class="login">
    {% block login %}

    {% if session['name'] is defined or session['logged_in'] is defined %}    
        <!-- if cookie exists -->

            {% if session['name'] == 'no-account-found-please-create-account' %}
            <!-- and the cookie is set to this wonky value because you need to see the login screen -->

                <form action='/createuser' method="POST">
                    <div class="form-group">
                    
                        <label for="name-field"></label>
                        <input type="text"
                            id="name-input"
                            name="name-input"




#*############################################################################*#
#*#                             CRUD                                         #*#
#*############################################################################*#
add something in ***CRUD**** to "find" existing profile records, so that you can increment qty

def get_profile_by_plantid_and_userid(plant_id, user_id):  #or just plant, user  ....?
"""Return existing profile (id?) by matching plantid and userid."""

  return Profile.query.filter(*some stuff here*).first()   #https://en.wikipedia.org/wiki/Magic_string



  IF A RECORD DOES ALREADY EXIST, AND YOU JUST NEED TO UPDATE THE QUANTITY COL LATER:

  def update_user_fname(user_id, name):
  """Update the fname of an existing user.
  
  The new name will be captured via user input field.

  >>> update_user_name("1", "jane")
  # TODO: update docstring
  """

  user = User.query.get(user_id)       #HOW TO UPDATE AN EXISTING RECORD COLUMN
  user.fname = name                   #ONCE YOU HAVE THE USER (LIKE A REFERENCING A VARIABLE, ONLY NOT?), YOUR CAN SET SPECIFIC COL TO A NEW VALUE
  db.session.commit()

  return user






  loop back to server.py .....



  