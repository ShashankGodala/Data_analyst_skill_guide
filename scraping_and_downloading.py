# importing libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml

# extract function with variable 'page', to iterate through the search pages
def extract(page):
    # url of website filtered for 'data analyst' jobs in australia
    url = f'https://au.indeed.com/jobs?q=data%20analyst&start={page}'
    r = requests.get(url)

    # using 'lxml' for html parsing
    soup = BeautifulSoup(r.content, 'lxml')
    return soup

# creating a prefix name with home page url
prefix = 'https://au.indeed.com'

# transform function to pull different attributes of jobs into different variables
def transform(soup):
    divs = soup.find_all('td', class_="resultContent")
    for item in divs:
        # extracting job title
        title = item.find('a').text.strip()

        # extracting the name of the company
        company = item.find('span', class_='companyName').text.strip()

        # extracting company or job location details
        company_location = item.find('div', class_='companyLocation').text.strip()

        # getting salary information if it is given or else 'None'
        try:
            salary = item.find('div', class_='metadata salary-snippet-container').text.strip()
        except:
            salary = ''

        # extracting the link to the job
        if item.find('a') is not None:
            links = item.find('a', class_='jcs-JobTitle css-jspxzf eu4oa1w0')['href']
        else:
            None

        # extracting the job description by going into the job details for all the jobs and scraping description text
        if item.find('a') is not None:
            # link given in href
            link = item.find('a', class_='jcs-JobTitle css-jspxzf eu4oa1w0')['href']
            #concatinating a prefix to the link
            full_url = prefix + str(link)
            # getting full description
            description = BeautifulSoup((requests.get(full_url).content), 'lxml').find('div', {'class': 'jobsearch-jobDescriptionText'}).text.strip()
        else:
            None
        # creating a dictionary for each job details
        job = {
            'title':title,
            'company':company,
            'location':company_location,
            'salary':salary,
            'link':links,
            'description':description
        }
        # inserting all the dictionaries into a list
        job_data.append(job)
    return

job_data = []

# each page is denoted by a number in link (ex: page 1 = 0, page 2 = 10,page 3 =20)
# iterating through all the pages and scraping the data
for i in range(0, 1800, 10):
    c = extract(i)
    transform(c)

# creating a dataframe with the list that containing the dictionaries of jobs
jobs_df = pd.DataFrame.from_records(job_data)
# exporting the data frame as a csv
jobs_df.to_csv('/Users/shashankgodala/PycharmProject/DataJobSearch/indeed_dataanalystjobs.csv')






