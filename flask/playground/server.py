from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def initial():
    return "enter http://localhost:5000/play to do something"

@app.route('/play')
def make_boxes():
    return render_template("playground1.html")

@app.route("/play/<number_of_boxes>")
def number_of_boxes(number_of_boxes):
    num_of_times = int(number_of_boxes)
    return render_template("playground2.html", num_of_times = num_of_times)
@app.route("/play/<number_of_boxes>/<string:color_change>")
def color_of_boxes(number_of_boxes,color_change):
    num_of_times = int(number_of_boxes)
    color_change = color_change
    return render_template("playground3.html", num_of_times = num_of_times, color_change = color_change)
if __name__ == "__main__":
    app.run(debug=True)