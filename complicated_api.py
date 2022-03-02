
import flask 
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["Debug"] = True

# create some data for our catalog in the form of a list of dictinories

books = [
    {'id': 'admin',
     'title': 'Hey This is Abhinav',
     'author': 'Abhinav Kumar',
     'first_sentence': 'Welcome to My API',
     'year_published': '02/03/2022'},
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

numbers = [
    {
        'id' : '1',
        'name':'abhinav'
    },
    {
        'id' : '2',
        'name':'ajay'
    },
    {
        'id' : '3',
        'name':'aakash'
    },
    {
        'id' : '4',
        'name':'aman'
    },
    
]

@app.route('/',methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# @app.route('/api/v1/resources/books/all',methods=['GET'])
# def api_all():
#     return jsonify(books)

@app.route('/num',methods=['GET'])
def api_one():
    return jsonify(numbers)

app.run()
