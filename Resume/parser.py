import os
import requests
from bs4 import BeautifulSoup as bs
from django import setup



class MyException(Exception):
    pass

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", r"D:\DjangoProjects\Engine_Resume\Engine_Resume\settings.py")
# setup()

base_url = 'https://github.com/MarberyUA?tab=repositories'

def github_parse(base_url):
    projects = []
    session = requests.Session()
    request = session.get(base_url)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        line = soup.find_all('div', attrs={'class': 'col-10 col-lg-9 d-inline-block'})
        for div in line:
            title = div.find('a', attrs={'itemprop': 'name codeRepository'}).text
            try:
                description = div.find('p', attrs={'itemprop': 'description'}).text
            except AttributeError:
                print('Description did not matched')
                description = 'Not matched'
            try:
                programm_language = div.find('span', attrs={'itemprop': 'programmingLanguage'}).text
            except AttributeError:
                print('Programme language did not matched')
                programm_language = 'Not matched'
            updated_time = div.find('relative-time', attrs={'class': 'no-wrap'}).text
            link = div.find('a', attrs={'itemprop': 'name codeRepository'})['href']
            projects.append({
                'title' : title.strip(),
                'description': description.strip(),
                'programm_language': programm_language,
                'update_time': updated_time,
                'link': link
            })
        return projects
    else:
        print('Error')



if __name__ == '__main__':

    new_one = github_parse(base_url)
    print(new_one)

