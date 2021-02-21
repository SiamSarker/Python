import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.body)
# print(soup.contents)
# print(soup.find_all('a'))
# print(soup.a)
# print(soup.find('a'))
print(soup.find(id='score_26208555'))