import statistics
from typing import List

from backend.berry.application.services.get_berry_by_id_response import GetBerryByIdResponse


class AllBerryStats:
    def __init__(self):
        pass

    @staticmethod
    def create_stats(berries: list[GetBerryByIdResponse]):
        names = [berry.name for berry in berries]
        growth_times = [berry.growth_time for berry in berries]
        growth_times_diff = {berry.growth_time for berry in berries}
        min_growth_time = min(growth_times)
        max_growth_time = max(growth_times)
        median_growth_time = round(statistics.median(growth_times), 2)
        variance_growth_time = round(statistics.variance(growth_times), 2)
        mean_growth_time = round(statistics.mean(growth_times), 2)
        frequency_growth_time = [{growth: growth_times.count(growth)} for growth in growth_times_diff]
        return {
            "berries_names": names,
            "min_growth_time": min_growth_time,
            "median_growth_time": median_growth_time,
            "max_growth_time": max_growth_time,
            "variance_growth_time": variance_growth_time,
            "mean_growth_time": mean_growth_time,
            "frequency_growth_time": frequency_growth_time,
        }

    @staticmethod
    def create_growth_times(data: list[GetBerryByIdResponse]) -> List[int]:
        return [berry.growth_time for berry in data]