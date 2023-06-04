import requests
from backend.shared.domain.repository import Repository


class PokeAPIRepository(Repository):

    def __init__(self):
        pass

    def get_all(self):
        url = "https://pokeapi.co/api/v2/berry/?offset=0&limit=1000"
        response = requests.get(url)

        if response.status_code == 200:
            json_data = response.json()
            return json_data

    def get_by_id(self, id: int):
        url = f"https://pokeapi.co/api/v2/berry/{id}"
        response = requests.get(url)

        if response.status_code == 200:
            json_data = response.json()
            return json_data
