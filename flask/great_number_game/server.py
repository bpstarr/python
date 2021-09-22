from flask import Flask,render_template, request, redirect,session
import random

app = Flask(__name__)
app.secret_key='secret'

@app.route('/')
def index():
    if 'message' not in session:
        session["message"] = ""
    if 'number' not in session:
        session['number'] =random.randint(1,100)
    return render_template("index.html",message=session['message'])

@app.route('/guess', methods=['POST'])    
def guess_answer():
    guess = int(request.form['number'])
    if guess == session['number']:
        session['message'] = "you win"
    if guess > session['number']:
        session['message'] = "too high, guess lower"
    elif guess < session['number']:
        session['message'] = "too low, guess higher"
    return redirect('/')
@app.route('/reset')
def reset():
    session['number']
    session.pop("number")
    session.pop("message")
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)