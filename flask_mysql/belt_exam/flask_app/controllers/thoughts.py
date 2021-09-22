from flask_app.models.thought import Thought
from flask_app.models.user import User
from flask_app import app 
from flask import render_template,redirect,request,flash,session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/create/thought', methods = ['POST'])
def create_thought():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Thought.thought_validator(request.form):
        return redirect('/dashboard')
    data = {
        "thought":request.form['thought'],
        "user_id":session["user_id"]
    }
    
    Thought.add_thought(data)
    return redirect('/dashboard')

@app.route('/like/int:<id>', methods =['POST'])
def like(id,like):
    if "user_id" not in session:
        return redirect('/logout')
    data = {
        "like":request.form [like],
    }
    Thought.like_or_unlike(data)
    return redirect('/dashboard')
@app.route('/dislike', methods =['POST'])
def dislike(id):
    if "user_id" not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    Thought.like_or_unlike(data)
    return redirect('/dashboard')

@app.route('/destroy/thought/<int:id>')
def destroy_thought(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id':id
    }
    Thought.delete_thought(data)
    return redirect('/dashboard')

@app.route('/users/<int:id>')
def show_users_thoughts(id):
    if "user_id" not in session:
        return redirect('/logout')
    users = {
        "id": id
    }

    return render_template("user_page.html", users = User.show_single_user(users), 
    thoughts = Thought.show_users_thoughts(users))

    

