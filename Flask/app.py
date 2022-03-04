from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hii Abhinav'

if __name__ == "__main__" :
    app.run(debug=True)

# # How to change the port

# if __name__ == "__main__" :
#     app.run(debug=True,port=8000)