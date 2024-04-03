from flask_app.init import app
from flask import render_template,request, redirect, session,flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

from flask_app import Bcrypt
bcrypt = Bcrypt(app)
#=========Display Route==========
@app.route('/')
def log_reg():
    return render_template('index.html')

#===========Action Route===========
@app.route('/users/register', methods=['post'])
def register():
    if not User.validate(request.form):
        return redirect('/')
    
    data={
        **request.form,
        'password':bcrypt.generate_password_hash(request.form['password'])
    }
    user=User.save_user(data)
    session['user_id']=user

    return redirect('/recipes')

#Login user with validate form
@app.route('/users/login',methods=['POST'])
def login():
    user_db = User.get_by_email(request.form)
    if not user_db:
        flash('Invalid email or password',"login")
        return redirect('/')
    if not bcrypt.check_password_hash(user_db.password, request.form['password']):
        flash('Invalid email or password',"login")
        return redirect('/')
    session['user_id']=user_db.id
    return redirect('/recipes')

#=========Display Route==========
@app.route('/recipes')
def dashboard():
    if 'user_id' not in session:#if he has not an id redirect to the register page
        return redirect('/')
    all_recipes = Recipe.get_recipes()
    user= User.get_by_id({'id': session['user_id']})
    return render_template('/dashboard.html',all_recipes=all_recipes,user=user)
#! ACTION ROUTE
# === Login ===
@app.route("/login", methods=["POST"])
def process_login():

    if not User.validate_login_user(request.form):
        return redirect("/")

    # see if the username provided exists in the database
    data = {"email": request.form["email"]}
    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/")

    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        # if we get False after checking the password
        flash("Invalid Email/Password", "login")
        return redirect("/")

    # get the user by his email
    session["user_id"] = user_in_db.id
    return redirect("/dashboard")


# * View Route
@app.route("/dashboard")
def dash():
    #! ROUTE GUARD
    if "user_id" not in session:
        return redirect("/")
    # grab the user id from session and put in a dictionary
    data = {"id": session["user_id"]}
    # grab the user by id from DB
    current_user = User.get_by_id(data)
    print("===> current_user:", current_user)
    return render_template("dashboard.html", username=current_user.first_name)


# LOGOUT


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
