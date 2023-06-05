from dataclasses import dataclass


@dataclass
class GetBerryByIdResponse:
    firmness: dict
    flavors: list
    growth_time: int
    id: int
    item: dict
    max_harvest: int
    name: str
    natural_gift_power: int
    natural_gift_type: dict
    size: int
    smoothness: int
    soil_dryness: int
