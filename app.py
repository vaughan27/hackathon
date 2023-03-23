from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    url = f'https://jobs.github.com/positions.json?description={query}'
    response = requests.get(url)
    jobs = response.json()
    return render_template('search.html',  jobs=jobs)
