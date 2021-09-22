from flask_app.models.latte import Latte
from flask_app.models.user import User
from flask_app import app
from flask import render_template,redirect,request,flash,session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/user/make_latte', methods = ['POST'])
def create_latte():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Latte.latte_validator(request.form):
        return redirect('/dashboard')
    data = {
        "name":request.form['name'],
        "filling":request.form['filling'],
        "crust":request.form['crust'],
        "user_id":session["user_id"]
    }
    
    Latte.create_latte(data)
    return redirect('/dashboard')

@app.route('/edit/<int:id>')
def get_to_edit_page(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id' : id
    }
    return render_template('edit.html', latte = Latte.show_single_latte(data))
@app.route('/update/latte', methods = ['POST'])
def update_latte():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Latte.latte_validator(request.form):
        return redirect('/dashboard')
    data = {
        "name":request.form['name'],
        "filling":request.form['filling'],
        "crust":request.form['crust'],
        "user_id":session["user_id"],
        "id" : request.form['id']
    }
    
    Latte.edit_latte(data)
    return redirect('/dashboard')
@app.route('/pies')
def get_all_pies():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('pies.html',all_pies_with_users = Latte.get_all_with_users())

@app.route('/show/<int:id>')
def display_show_and_vote_page(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }      
    return render_template('show_and_vote.html', user_with_latte = Latte.get_latte_with_user(data))

@app.route('/vote/<int:id>', methods = ['POST'])
def vote(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : id
    }
    print(Latte.cast_vote(data))
    return redirect('/pies')
    
@app.route('/destroy/<int:id>')
def destroy(id):
    data = {
        "id":id
    }
    Latte.destroy(data)
    return redirect ('/dashboard')

