from flask_app import app
from flask import render_template,request,redirect 
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/create_new_ninja')
def create_new_ninja_page():
    dojos = Dojo.get_all()
    return render_template('New_ninjas.html',dojos = dojos)
@app.route('/created_new_ninja', methods = ['POST'])
def create_new_user():
    data = {
        "dojo_id":request.form['dojo_id'],
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "age":request.form['age']
    }
    Ninja.save(data)
    return redirect("/created_new_ninja")