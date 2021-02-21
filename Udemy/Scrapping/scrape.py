import requests
from bs4 import BeautifulSoup
import pprint

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
# votes = soup.select('.score')
subtext = soup.select('.subtext')

# print(votes[0].get('id'))


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            print(points)
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    return hn


pprint.pprint(create_custom_hn(links, subtext))