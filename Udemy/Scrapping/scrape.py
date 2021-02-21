import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.body)
# print(soup.contents)
# print(soup.find_all('a'))
# print(soup.a)
# print(soup.find('a'))
# print(soup.find(id='score_26208555'))
# print(soup.select('.score'))
# print(soup.select('#score_26208555'))

links = soup.select('.storylink')
votes = soup.select('.score')

print(votes[0].get('id'))