import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.com/jobs?q=python+developer&l=New+York"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

job_listings = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

for job in job_listings:
    title = job.find("a", {"class": "jobtitle"})["title"]
    company = job.find("span", {"class": "company"}).text.strip()
    location = job.find("span", {"class": "location"}).text.strip()
    salary = job.find("span", {"class": "salaryText"})
    if salary:
        salary = salary.text.strip()
    else:
        salary = "N/A"
    description = job.find("div", {"class": "summary"}).text.strip()
    
    # Store the information in a dictionary or a pandas dataframe
    job_posting = {"title": title, "company": company, "location": location, "salary": salary, "description": description}
