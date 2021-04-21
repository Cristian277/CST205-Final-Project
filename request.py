import requests, json
from pprint import pprint

my_key = 'c5d329154c6814866283f9572098cff2'

payload = {
  'api_key': my_key,
  'start_date': '2021-04-21',
  'end_date': '2021-04-24'
}
#endpoint = 'https://api.nasa.gov/planetary/apod'
endpoint = 'https://api.themoviedb.org/3/movie/550'
try:
  r = requests.get(endpoint, params=payload)
  data = r.json()
  pprint(data)
except:
  print('please try again')