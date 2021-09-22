from flask_app import app 
from flask import render_template,redirect,request,flash,session
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/new/recipe')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_recipe.html', user = User.show_single_user(data))

@app.route('/create/recipe', methods = ['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.recipe_validator(request.form):
        return redirect('/new/recipe')
    data = {
        'name':request.form["name"],
        'description':request.form['description'],
        'instructions':request.form['instructions'],
        'made_in_under_30mins':int(request.form['made_in_under_30mins']),
        'date_made':request.form['date_made'],
        'user_id':request.form['user_id']
    }
    Recipe.add_recipe(data)
    return redirect('/dashboard')

@app.route('/edit/recipe/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id" : id
    }
    user_data = {
        "id" :session["user_id"]
    }
    return render_template("edit_recipe.html", edit = Recipe.show_single_recipe(data), user = User.show_single_user(user_data))

@app.route('/update/recipe',methods = ['POST'])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.recipe_validator(request.form):
        return redirect('/new/recipe')
    data = {
        'name':request.form["name"],
        'description':request.form['description'],
        'instructions':request.form['instructions'],
        'made_in_under_30mins':int(request.form['made_in_under_30mins']),
        'date_made':request.form['date_made'],
        'id':request.form['id']
    }
    Recipe.edit_recipe(data)
    return redirect('/dashboard')

@app.route('/recipe/<int:id>')
def show_recipe(id):
    if "user_id" not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session["user_id"]
    }
    print('user_data')
    return render_template("show_single_recipe.html", recipe = Recipe.show_single_recipe(data),user=User.show_single_user(user_data))

@app.route('/destroy/recipe/<int:id>')
def destroy_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id':id
    }
    Recipe.delete_recipe(data) 
    return redirect('/dashboard')