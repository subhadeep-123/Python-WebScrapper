import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hmlist):
    sorted_data = sorted(hmlist, key=lambda x: x['Votes'], reverse=True)
    print(type(sorted_data), len(sorted_data))
    return to_json(sorted_data)


def create_custom_hm(links, subtext):
    hm = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 100:
                hm.append({'title': title, 'links': href, 'Votes': points})
    return sort_stories_by_votes(hm)


def to_json(sorted_data):
    with open("data.json", 'w') as file:
        json.dump(sorted_data, file)


pprint(create_custom_hm(links, subtext))
