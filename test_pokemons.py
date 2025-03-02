import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '9d68d333bad1b482a4666f2aab1bdf71'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '22717'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Бульбозавр'

@pytest.mark.parametrize('key, value', [('name', 'Бульбозавр'), ('trainer_id', TRAINER_ID), ('pokemon_id', '248560')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
