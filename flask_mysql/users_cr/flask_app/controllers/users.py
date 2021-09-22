from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

@app.route("/users")
def read():
    users = User.get_all()
    print(users)
    return render_template("read(all).html",users = users)
@app.route("/users/new")
def create_userpage():
    return render_template("create.html")
@app.route("/create_user", methods = ['POST'])
def create_user():
    data = {
        "fname":request.form["first_name"],
        "lname":request.form["last_name"],
        "email":request.form["email"]
    }
    User.save(data)
    return redirect('/users/new')
@app.route("/users/<id>")
def show_single_user(id):
    data = {
        "chosen_Id" : id
    }
    thisUser = User.show_single_user(data)
    return render_template('read(one).html',user = thisUser )
@app.route("/users/<id>/edit")
def update_single_user(id):
    data = {
        "chosen_Id" : id
    }
    thisUser = User.show_single_user(data)
    return render_template("edit.html", user = thisUser)
@app.route("/edit_user/<id>", methods = ["POST"])
def edit_user(id):
    data = {
        "fname":request.form["first_name"],
        "lname":request.form["last_name"],
        "email":request.form["email"],
        "chosen_Id" : id
    }
    User.edit_user(data)
    return redirect(f"/users/{id}/edit")
@app.route('/delete_user/<id>')
def delete_user(id):
    data = {
        "chosen_id" : id
    }
    User.delete_user(data)
    return redirect("/users")
