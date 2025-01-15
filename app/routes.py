from app import app
from flask import render_template
from flask import Flask, url_for


@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/stocks')
def stocks():
    return render_template('stocks.html')

@app.route('/login')
def login():
    return render_template('login.html')

