import requests
from bs4 import BeautifulSoup

def courses (year,season):
    names_of_courses = []
    link = f'http://students.iposov.spb.ru/{str(year)}{season}/'
    response = requests.get(link).text
    html = BeautifulSoup(response, features="html.parser")
    section = html.find('section',{'class':'main-content'})
    ul = section.find('ul')
    ul2 = ul.find_all('ul')
    for i in range (len(ul2)):
        li = ul2[i].find_all('li')
        for j in range (len(li)):
            names_of_courses.append(li[j].find('a').text)
    return names_of_courses
#print(courses(19,'fall'))


def animals (name, part):
    response = requests.get(f'https://ru.wikipedia.org/wiki/{name}').text
    html = BeautifulSoup(response, features="html.parser")
    all = html.find('table')
    div = all.find_all('div', {'class': 'ts-Taxonomy-rang-row'})
    for i in range(len(div)):
        div_deeper = div[i].find('div', {'class':'ts-Taxonomy-rang-label'})
        if div_deeper.text.replace(':','') == part:
            ans = div[i].find('div', {'class':'ts-Taxonomy-rang-name'})
            return ans.text.replace(':','')

def animals_1 (name):
    response = requests.get(f'https://ru.wikipedia.org/wiki/{name}').text
    html = BeautifulSoup(response, features="html.parser")
    all = html.find('table')
    tb = all.find('tbody')
    td = tb.find('td', {'class':'plainlist'})
    div = td.find_all('div', {'class':'ts-Taxonomy-rang-row'})
    ans = {}
    for i in div:
        animal_class = i.find('div', {'class': 'ts-Taxonomy-rang-label'})
        animal_name = i.find('div', {'class': 'ts-Taxonomy-rang-name'})
        ans[animal_class.text.replace(':','')]=animal_name.text.replace(':','')
    return ans

#print(animals('Осьминоги', 'Домен'))
#print(animals_1('Осьминоги'))
'''
def wiki (link, counter = 0, ans):
    counter +=1
    if counter > 100 or link in ans:
        return list(ans)
    response = requests.get(link).text
    html = BeautifulSoup(response, features='html.parser')
    div = html.find('div', {'class': 'mw-parser-output'})
'''
