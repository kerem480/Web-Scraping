import requests
from bs4 import BeautifulSoup


html=requests.get("https://www.imdb.com/chart/top/").text
soup=BeautifulSoup(html,"lxml")
jobs=soup.find_all("td",class_="titleColumn")
for job in jobs:

    film_name=job.find("a").text
    point=soup.find("td",class_="ratingColumn imdbRating")
    film_rate=point.find("strong").text

    print(f'''
    Film Name: {film_name}
    ****************************
    Film Rate: {film_rate}
    ''')

