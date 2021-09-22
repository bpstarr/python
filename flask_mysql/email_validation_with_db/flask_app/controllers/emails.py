from flask_app import app
from flask import render_template,request,redirect,flash
from flask_app.models.email import Email


@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/register',methods = ['POST'])
def register():
    data = {
        'email': request.form['email']
    }
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.create_email(data)
    print('New Email')
    return redirect('/success')
    
@app.route('/success')
def show_emails(email):
    results = Email.get_all()
    return render_template('success.html',results = results,)
        