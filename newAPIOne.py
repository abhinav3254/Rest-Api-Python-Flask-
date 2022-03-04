


from flask import Flask

app = Flask(__name__)

kolkata_features = [
    {
        'long':'22.5726° N',
        'lat':'88.3639° E'
    },
    {
        'lang':'Bengali',
        'Country':'India'
    }

]
mumbai = [
    {
        'long':'20.5726° N',
        'lat':'60.3639° E'
    },
    {
        'lang':'Marathi',
        'Country':'India'
    }

]
@app.route('/ccu')
def kolkata():
    return kolkata_features

@app.route('/mumbai')
def kolkata_all() :
    return mumbai

if __name__ == "__main__" :
    app.run(debug=True)
