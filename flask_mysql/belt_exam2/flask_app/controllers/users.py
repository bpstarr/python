
from flask_app import app 
from flask import render_template,redirect,request,flash,session
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.latte import Latte
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/register', methods = ['POST'])
def register_user():
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':request.form['password'],
        'verify_password':request.form['verify_password']
    }
    valid = User.user_validator(data)
    if valid:
        hashed_pw = bcrypt.generate_password_hash(request.form['password'])
        data['hashed_pw'] = hashed_pw
        user = User.add_user(data)
        print(user)
        session['user_id'] = user
        print('User logged in.')
    return redirect('/dashboard')
@app.route('/user/login', methods = ['POST'])
def login_user():
    user = User.get_by_email(request.form)
    if not user:
        flash("Invalid email or password")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid email or password")
        return redirect('/')
    session['user_id'] = user.id
    print("Successful login")
    return redirect ('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
            "id" : session['user_id']
        }
    return render_template('dashboard.html', users = User.show_single_user(data), users_lattes = Latte.show_users_lattes(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')