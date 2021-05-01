# forms.py
from wtforms import Form, StringField, SelectField

class MovieSearchForm(Form):
    search = StringField('Search for Movie: ')