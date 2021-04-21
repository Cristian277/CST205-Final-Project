import requests, json
from pprint import pprint
from flask import Flask, render_template 
from flask_bootstrap import Bootstrap

app = Flask(__name__)
boostrap = Bootstrap(app)

my_key = 'c5d329154c6814866283f9572098cff2'

parameters = {
  'api_key': my_key,
}

endpoint = 'https://api.themoviedb.org/3/movie'

#This is going to be super important once we retrieve the correct data
#Plan is go into the view the view will have a post form that sends the movie you're looking for
#as a parameter to our search function we then try to look for it with the code right above
#if it works then load the page with the results by using the code right below this.
#also have a way to get back to home we should have nagivation
#data = json.load(open('cs_people.json'))

#Home Route
@app.route('/')
def hello():
    try:
        r = requests.get(endpoint, params=payload)
        data = r.json()
        pprint(data)
    except:
        print('please try again')
    
    ourData = json.load(open(data))

    return render_template('index.html')


#Second Page Route
@app.route('/page2')
def p2():
    return render_template('page2.html')



