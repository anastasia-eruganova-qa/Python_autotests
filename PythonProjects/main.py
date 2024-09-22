import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'dff38a046564a2282a7181059bb77d5c'
HEADER = {'Content-Type': 'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "yeryganova90@bk.ru",
    "password": "Iloveqa122"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_name = {
    "pokemon_id": "73286",
    "name": "Pusy",
    "photo_id": 2
} 

body_catch = {
    "pokemon_id": "9"
}



'''response_create = requests.post(url = ,f'{URL}/pokemons' headers = HEADER, json = body_create )
print(response_create.text)'''

'''message = response_create.json()['message']
print(message)'''

'''response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)'''

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)
