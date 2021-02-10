from bs4 import BeautifulSoup
import  requests

html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text

# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
# jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
    company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')

    skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
    published_date = job.find('span', class_ = 'sim-posted').span.text
    print(f'''
    Company name: {company_name}
    Required Skills: {skills}
    ****************
    ''')
    
# print(skills)
# print(company_name)
# print(published_date)

# print(f'''
# Company name: {company_name}
# Required Skills: {skills}
# ''')


