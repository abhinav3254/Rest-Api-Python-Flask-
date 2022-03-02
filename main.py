from distutils.log import debug
from flask import Flask , jsonify

#  copy pasted from https://flask.palletsprojects.com/en/2.0.x/quickstart/

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, Abhinav Welcome to API!"

def sum (a,b):
    return a+b

def avg (a,b):
    return (a+b)/2


@app.route("/even/<str:n>")
def even(a):
    b = a%2
    if(b==0):
        return True
    else:
        return False



if __name__ == "__main__":
    app.run(debug==True)