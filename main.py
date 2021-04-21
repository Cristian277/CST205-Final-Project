
from flask import Flask, render_template 
from flask_bootstrap import Bootstrap

app = Flask(__name__)
boostrap = Bootstrap(app)

#Home Route
@app.route('/')
def hello():
    random.shuffle(image_info)
    return render_template('index.html')


#Second Page Route
@app.route('/page2')
def p2():
    return render_template('page2.html')



