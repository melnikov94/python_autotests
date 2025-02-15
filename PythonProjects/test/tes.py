import requests
import json

# Базовый URL API
BASE_URL = 'https://api.pokemonbattle.ru/v2'

# Заголовки для авторизации и контента
headers = {
    'trainer_token': 'a0acddbae731ac6dad649b9c62ad3bba',
    'Content-Type': 'application/json'
}

# 1. Создание покемона
create_pokemon_url = f"{BASE_URL}/pokemons"
create_pokemon_data = {
    "name": "Бульбазавр",
    "photo_id": 1
}

response_create = requests.post(create_pokemon_url, headers=headers, data=json.dumps(create_pokemon_data))
print("Создание покемона:")
print(response_create.json())

# 2. Смена имени покемона
update_pokemon_url = f"{BASE_URL}/pokemons"
update_pokemon_data = {
    "pokemon_id": "195379",
    "name": "New Name",
    "photo_id": 2
}

response_update = requests.put(update_pokemon_url, headers=headers, data=json.dumps(update_pokemon_data))
print("\nСмена имени покемона:")
print(response_update.json())

# 3. Поймать покемона в покебол
add_pokeball_url = f"{BASE_URL}/trainers/add_pokeball"
add_pokeball_data = {
    "pokemon_id": "195382"
}

response_add_pokeball = requests.post(add_pokeball_url, headers=headers, data=json.dumps(add_pokeball_data))
print("\nПоймать покемона в покебол:")
print(response_add_pokeball.json())