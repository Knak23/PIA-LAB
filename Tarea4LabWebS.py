import csv
import requests
from bs4 import BeautifulSoup

url2 = "https://realpython.github.io/fake-jobs/"
page = requests.get(url2)
soup = BeautifulSoup(page.content, "html.parser")


results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
jobs = list()
for job in job_elements:
    jobs.append(job.text)

python_jobs = results.find_all(
    "h2", string = lambda text: "python" in text.lower()
)
fjobs = list()

python_jobs_elements = [ 
    h2_element.parent.parent.parent for h2_element in python_jobs
    ]

for job_element in python_jobs_elements:
        title_element = job_element.find("h2", class_="title")
        fjobs.append(title_element.text.strip())
        company_element = job_element.find("h3", class_="company")
        fjobs.append(company_element.text.strip())
        location_element = job_element.find("p", class_="location")
        fjobs.append(location_element.text.strip())
        link_url = job_element.find_all("a")[ 1 ] ["href"]
        fjobs.append(link_url)

for t in zip(jobs,fjobs):
    print(t)

with open("./WebScraping.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, dialect = "excel")
    csv_writer.writerows(zip(jobs, fjobs))
    
