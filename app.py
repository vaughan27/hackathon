from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()


# Set the API endpoint URL
url = 'https://api.indeed.com/ads/apisearch'

# Set the parameters for your search
params = {
    'publisher': 'YOUR_PUBLISHER_ID',
    'q': 'python developer',
    'l': 'New York',
    'sort': 'date',
    'format': 'json',
    'v': '2'
}

# Make a GET request to the API endpoint
response = requests.get(url, params=params)

# Parse the response JSON
response_json = json.loads(response.content)

# Extract the job titles from the response
job_titles = [result['jobtitle'] for result in response_json['results']]

# Print the job titles
for job_title in job_titles:
    print(job_title)
