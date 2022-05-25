from decorator import parametrized_decor
import requests


url = "https://superheroapi.com/api/2619421814940190/search/"
heronames = [{'name' : 'Hulk'}, {'name' : 'Captain America'}, {'name' : 'Thanos'}]
path = 'C:\\Users\\f.burov\\Desktop\\logs.txt'



@parametrized_decor(parameter=path)
def intelligence():
    for name in heronames:
        hero_r = requests.get(url + name['name'])
        name['intelligence'] = int(hero_r.json()['results'][0]['powerstats']['intelligence'])
    new_dict = sorted(heronames, key=lambda name: -name['intelligence'])
    iq = new_dict[0]['name']
    return f'Самый умный супергерой {iq}'


intelligence()


