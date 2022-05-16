from decorator import logger
import requests

url = "https://superheroapi.com/api/2619421814940190/search/"
heronames = [{'name' : 'Hulk'}, {'name' : 'Captain America'}, {'name' : 'Thanos'}]


def intelligence():
    for name in heronames:
        hero_r = requests.get(url + name['name'])
        name['intelligence'] = int(hero_r.json()['results'][0]['powerstats']['intelligence'])
    new_dict = sorted(heronames, key=lambda name: -name['intelligence'])
    iq = new_dict[0]['name']
    return f'Самый умный супергерой {iq}'


result = logger(intelligence)
result()

