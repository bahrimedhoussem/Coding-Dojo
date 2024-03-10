from flask_app import app
from flask import render_template,redirect , request 
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    data={
        "first_name":request.form['first_name'],
        "last_name" :request.form['last_name'],
        "age":request.form['age'],
        "dojos_id":request.form['dojos_id']
    }
    Ninja.save(data)
    return redirect('/ninjas')



@app.route('/ninjas')
def dashboar_ninja():

    return render_template("ninja_page.html")

@app.route('/dojos/<int:ninja_id>')
def show(ninja_id):
    ninja=Ninja.get_one(ninja_id)
    return render_template("show_ninja.html",ninja=ninja)

