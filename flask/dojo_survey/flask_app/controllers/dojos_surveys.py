from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojos_survey import Dojo_survey

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/users', methods= ['POST'])
def save_answers():
    data = {
        "name":request.form['name'],
        "location":request.form['location'],
        "language":request.form['language'],
        "comment":request.form['comment']   
    }
    if not Dojo_survey.validate_survey_answers(request.form):
        return redirect('/')
    Dojo_survey.save(data)
    print("Got post info")
    return redirect('/results')
@app.route('/results')
def results ():
    dojo_answers = Dojo_survey.get_all()
    return render_template("results.html", dojo_answers = dojo_answers)

