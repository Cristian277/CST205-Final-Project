"""
Cristian Arredondo
CST205
This creates a site where it displays 3 random images on the home page
if the user clicks on one of the 3 images they get more details on the image
the user then has the option to go back to the home page.
"""

from image_info import image_info
from PIL import Image
from flask import Flask, render_template 
from flask_bootstrap import Bootstrap
import random

app = Flask(__name__)
boostrap = Bootstrap(app)

#Home Route
@app.route('/')
def hello():
    random.shuffle(image_info)
    return render_template('index.html',my_list=image_info)

#Passing in the imageID and using pillow to get image information and then passing 
#all of the info to the page2.html view
@app.route('/page2/<imageID>')
def p2(imageID):
    chosenImageList = []
    pillowInfo = {}

    for i in image_info:
        if i['id'] == imageID:
            dictionary_copy = i.copy()
            chosenImageList.append(dictionary_copy)

            im = Image.open("static/images/" + i['id'] + ".jpg")

            pillowInfo['format'] = im.format
            pillowInfo['mode'] = im.mode
            pillowInfo['width'] = im.width
            pillowInfo['height'] = im.height

    return render_template('page2.html', my_list=chosenImageList,my_dictionary = pillowInfo)


