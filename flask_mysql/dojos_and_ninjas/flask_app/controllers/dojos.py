from flask_app import app
from flask import render_template,request,redirect 
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def get_index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('Dojos.html', dojos = dojos)
@app.route('/create_new_dojo', methods = ['POST'])
def create_new_dojo():
    data = {
        "name": request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')
@app.route('/dojos/<id>')
def show_dojo_and_ninjas(id):
    data = {
        "chosen_id": id
    }
    this_dojo = Dojo.show_dojo_and_ninjas(data)
    return render_template('show.html', users_in_dojo = this_dojo)


