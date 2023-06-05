from dataclasses import dataclass


@dataclass
class GetAllBerryStatsResponse:
    berries_names: list
    frequency_growth_time: list
    max_growth_time: int
    mean_growth_time: float
    median_growth_time: int
    min_growth_time: int
    variance_growth_time: float
