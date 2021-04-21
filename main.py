import requests, json
from pprint import pprint
from flask import Flask, render_template 
from flask_bootstrap import Bootstrap

app = Flask(__name__)
boostrap = Bootstrap(app)

"""
my_key = 'c5d329154c6814866283f9572098cff2'
parameters = {
  'api_key': my_key,
}
endpoint = 'https://api.themoviedb.org/3/movie/'
"""

#Home Route
@app.route('/')
def hello():
    try:
        response = requests.get("https://api.themoviedb.org/3/movie/550?api_key=c5d329154c6814866283f9572098cff2")
        print(response.json())
    except:
        print('please try again')

    return render_template('index.html')


#Second Page Route
@app.route('/page2')
def p2():
    return render_template('page2.html')



