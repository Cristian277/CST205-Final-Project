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
<img src= "'/images/ + {{data['results'][i]['poster_path']}} + '"/>
"""


#Home Route
@app.route('/')
def hello():
    listOfImages = []
    try:
        response = requests.get("https://api.themoviedb.org/3/movie/popular/?api_key=c5d329154c6814866283f9572098cff2")
        print(response.json())
        data = response.json()
        for i in range(0,9):
            listOfImages.append("https://image.tmdb.org/t/p/w300" + data['results'][i]['poster_path'])
    except:
        print('please try again')

    return render_template('index.html',data=data, images = listOfImages)


#Second Page Route
@app.route('/page2')
def p2():
    return render_template('page2.html')



