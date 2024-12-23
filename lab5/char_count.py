import requests

def get_character_count():
    url = "https://rickandmortyapi.com/api/character"
    response = requests.get(url)
    data = response.json()
    return data["info"]["count"]
char_count = get_character_count()
print(char_count)

