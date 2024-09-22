import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'dff38a046564a2282a7181059bb77d5c'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '4996'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
        response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
        assert response_get.json()["data"][0]["name"] == 'Бульбазавр'


@pytest.mark.parametrize('key, value' ,[('name' ,'Бульбазавр'), ('trainer_id', TRAINER_ID),('id','73522')])
def test_parametrize(key, value):
      response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
      assert response_parametrize.json()["data"][0][key] == value