from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def standard_checkerboard():
    return render_template("checkerboard.html", across = 8, down = 8)

@app.route('/<num>')
def number_of_boxes_down(num):
    return render_template('checkerboard.html',across = 8, down = int(num))

@app.route('/<num1>/<num2>')
def number_of_boxes_down_and_across(num1,num2):
    return render_template('checkerboard.html', across = int(num1), down= int(num2))

@app.route('/<num1>/<num2>/<colx>/<coly>')
def num_and_col_of_boxes(num1,num2,colx,coly):
    return render_template('checkerboard.html',across = int(num1), down = int(num2), colx = colx, coly = coly)

if __name__ == "__main__":
    app.run(debug=True)