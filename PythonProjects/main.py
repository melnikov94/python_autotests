import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN ="a62a"
HEADER = {"content-type":"application/json"  }

body_confirmation = {
}
"trainer_token": TOKEN
body_create = {
"пате": "Бульбазавр",
"photo": "801.png"
***response = requests.post(url = f'{URL}/trainers/reg", headers-HEADER, json body_registration) print(response.text)***
**'response_confirmation requests.post(url = f'(URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)***
response_create= requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
message= response_create.json()['message']
print(message)