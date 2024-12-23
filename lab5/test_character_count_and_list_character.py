import requests
import pytest
from char_count import get_character_count

list_charter = []
def test_rick_morty_charters_count():
    total_charter = get_character_count()
    url = "https://rickandmortyapi.com/api/character"
    count = 0
    while url:
        response = requests.get(url)
        data = response.json()
        count += len(data["results"])
        list_charter.extend(char["name"]
        for char in data["results"])
        url = data["info"]["next"]

    assert count == total_charter
    print(" Кол-во персонажей:", total_charter, "Из:", count)
    for character in list_charter:
        print(character)
