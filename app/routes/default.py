from app import app
from flask import render_template

# This is for rendering the home page

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/getmotivation')
def getmotivation():
    return render_template('getmotivation.html')

@app.route('/insecure')
def insecure():
    return render_template('insecure.html')

@app.route('/stuck')
def stuck():
    return render_template('stuck.html')