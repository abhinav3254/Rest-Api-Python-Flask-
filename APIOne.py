

import flask
from flask import jsonify


app = flask.Flask(__name__)
app.config["Debug"] = True

names = [
    {
        'name':'abhinav',
        'class':'B.Tech'
    },
    {
        'name':'Aman',
        'class':'Bussiness'
    },
    {
        'name':'Ajay',
        'class':'Flutter'
    },
    {
        'name':'Ravi',
        'class':'Commerce'
    }
]

@app.route('/',methods=['GET'])
def api_one():
    return jsonify(names)

app.run()