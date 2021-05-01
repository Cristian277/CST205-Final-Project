import requests, json
from pprint import pprint
from flask import Flask, render_template, redirect, url_for, request 
from flask_bootstrap import Bootstrap
from wtforms import Form, StringField, SelectField

app = Flask(__name__)
boostrap = Bootstrap(app)

class MovieSearchForm(Form):
    search = StringField('Search for Movie: ')

#Home Route
@app.route('/', methods=['GET', 'POST'])
def hello():

    search = MovieSearchForm(request.form)

    if request.method == 'POST':
        return search_results(search)

    listOfImages = []

    try:
        response = requests.get("https://api.themoviedb.org/3/movie/popular/?api_key=c5d329154c6814866283f9572098cff2")
        data = response.json()
        for i in range(0,9):
            listOfImages.append("https://image.tmdb.org/t/p/w300" + data['results'][i]['poster_path'])
    except:
        print('please try again')

    return render_template('index.html', data=data, images = listOfImages, form=search)


#Second Page Route
@app.route('/page2')
def p2():
    title = request.args.get('title', None)
    description = request.args.get('desc', None)
    release = request.args.get('release', None)
    popularity = request.args.get('popularity', None)
    image = request.args.get('image', None)
    return render_template('page2.html', title = title, desc = description, release = release, popularity = popularity, image = image)


@app.route('/results')
def search_results(search):

    listOfImages = []

    search_string = search.data['search'] #NAME OF THE MOVIE
    newSearchString = search_string.replace(" ","%20")

    #TRYING TO REQUEST FROM THE API IF IT WORKS THEN RENDER THE RESULTS PAGE AND PASS IN THE RESULT
    response = requests.get("https://api.themoviedb.org/3/search/movie?api_key=c5d329154c6814866283f9572098cff2&language=en-US&query=" + newSearchString + "&page=1&include_adult=true")
    print(response.json())
    data = response.json()
    length = len(data['results'])

    for i in range(0,length):
        listOfImages.append("https://image.tmdb.org/t/p/w300" + data['results'][i]['poster_path'])
 
    return render_template('results.html', data=data, images = listOfImages, sizeOfList=length)


