from app import app
from flask import render_template
from flask import Flask, url_for
from generate_graph import generate_graph


@app.route('/')
@app.route('/index')
def index():
    graph_html = generate_graph("^GSPC")
    return render_template('home.html', graph_html=graph_html)

@app.route('/stocks')
def stocks():
    return render_template('stocks.html')

@app.route('/login')
def login():
    return render_template('login.html')

