import json

from backend.shared.domain.repository import Repository


class FakeRepository(Repository):
    def get_by_id(self, id: int):
        result = {
            "firmness": {
                "name": "soft",
                "url": "https://pokeapi.co/api/v2/berry-firmness/2/"
            },
            "flavors": [
                {
                    "flavor": {
                        "name": "spicy",
                        "url": "https://pokeapi.co/api/v2/berry-flavor/1/"
                    },
                    "potency": 10
                },
                {
                    "flavor": {
                        "name": "dry",
                        "url": "https://pokeapi.co/api/v2/berry-flavor/2/"
                    },
                    "potency": 0
                },
                {
                    "flavor": {
                        "name": "sweet",
                        "url": "https://pokeapi.co/api/v2/berry-flavor/3/"
                    },
                    "potency": 0
                },
                {
                    "flavor": {
                        "name": "bitter",
                        "url": "https://pokeapi.co/api/v2/berry-flavor/4/"
                    },
                    "potency": 0
                },
                {
                    "flavor": {
                        "name": "sour",
                        "url": "https://pokeapi.co/api/v2/berry-flavor/5/"
                    },
                    "potency": 0
                }
            ],
            "growth_time": 3,
            "id": 1,
            "item": {
                "name": "cheri-berry",
                "url": "https://pokeapi.co/api/v2/item/126/"
            },
            "max_harvest": 5,
            "name": "cheri",
            "natural_gift_power": 60,
            "natural_gift_type": {
                "name": "fire",
                "url": "https://pokeapi.co/api/v2/type/10/"
            },
            "size": 20,
            "smoothness": 25,
            "soil_dryness": 15,
        }
        return result

    def get_all(self):
        result = {
            "results": [
                {"name": "cheri", "url": "https://pokeapi.co/api/v2/berry/1/"},
                {"name": "chesto", "url": "https://pokeapi.co/api/v2/berry/2/"}
            ]}
        return result