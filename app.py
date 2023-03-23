import json
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/A')
def hello_world():
    return 'Hello, World!'



@app.route('/jobs')
def jobs():
    publisher_id = 'c4f7f56214793037f6c572f6e3c021e88def5715a91d20e4fdac28fd1859da3f'
    api_key = 'K07oceIgQVcOyutXP8qhROGsF8tijSdRUVWvzpKyRGYP6NNHHNF18Voa7u17tmlZ'
    search_params = {
        'publisher': publisher_id,
        'q': 'python',
        'l': 'San Francisco',
        'jt': 'fulltime',
        'limit': 10,
        'format': 'json',
        'v': '2'
    }
    response = requests.get('http://api.indeed.com/ads/apisearch', params=search_params)
    jobs = response.json()['results']
    return render_template('jobs.html', jobs=jobs)