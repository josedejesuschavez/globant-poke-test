import requests
from backend.shared.domain.repository import Repository
from backend.shared.infraestructure.cache import cache


class PokeAPIRepository(Repository):

    def __init__(self):
        pass

    @cache.memoize(timeout=120)
    def get_all(self):
        url = "https://pokeapi.co/api/v2/berry/?offset=0&limit=1000"
        response = requests.get(url)

        if response.status_code == 200:
            json_data = response.json()
            return json_data

    @cache.memoize(timeout=120)
    def get_by_id(self, id: int):
        url = f"https://pokeapi.co/api/v2/berry/{id}"
        response = requests.get(url)

        if response.status_code == 200:
            json_data = response.json()
            return json_data
