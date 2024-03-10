from flask_app import app
from flask import render_template,redirect , request 
from flask_app.models.dojo import Dojo



@app.route('/dojos/create', methods=['POST'])
def create():
    Dojo.save(request.form)
    return redirect('/dojos')


@app.route('/dojos')
def dashboard():
    all_dojos = Dojo.get_all()
    print(all_dojos)
    return render_template("dojo_page.html", dojos=all_dojos)

