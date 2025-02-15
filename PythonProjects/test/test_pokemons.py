
import requests import pytest
URL = 'https://api.pokemonbattle.me/v2'
TOKEN=
'a0acddbae731ac6dad649b9c62ad3bba'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN} TRAINER_ID = '3650'

def test_status_code():
response = requests.get(url = f'{URL}/pokemons',
                         params = {'trainer_id' : TRAINER_ID})
assert response.status_code == 200
def test_part_of_response():
response_get = requests.get(url = f'{URL}/pokemons',
                             params = {'trainer_id' : TRAINER_ID})
assert response_get.json()["data"][0]["name"] == 'Бульбазавр'