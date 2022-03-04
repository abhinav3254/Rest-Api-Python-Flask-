# from flask import Flask

# How to render in HTML Page

from operator import index
from flask import Flask , render_template


app = Flask(__name__)

@app.route('/')
# def hello_world():
#     return 'Hii Abhinav'
# HTML render stuff doing Here
def hello_world():
    return render_template('index.html')

@app.route('/products')
def products():
    return 'products page'

if __name__ == "__main__" :
    app.run(debug=True)

# # How to change the port

# if __name__ == "__main__" :
#     app.run(debug=True,port=8000)