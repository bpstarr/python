from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"
@app.route('/dojo')
def dojo():
    return "Dojo!"
@app.route('/hi/<string:name>')
def hi(name):
    print(name)
    return "Hi " + name
@app.route('/repeat/<int:num>/<string:string>')
def repeat(num,string):
    return string * num
@app.route('/',defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response.Try again.'
if __name__ == "__main__":
    app.run(debug=True)