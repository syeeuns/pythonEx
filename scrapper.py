import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20201025',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > .list_ranking > tbody > tr')

for movie in movies:
    a_tag = movie.select_one('.title > div > a')
    if a_tag != None:
        rank = movie.select_one('.ac > img')['alt']
        rate = movie.select_one('.point')
        print(rank, a_tag.text, rate.text)
