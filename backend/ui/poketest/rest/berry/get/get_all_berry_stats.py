import statistics

from flask import Blueprint, render_template
from backend.berry.infraestructure.pokeapi_repository import PokeAPIRepository
from backend.ui.poketest.cache import cache
from backend.ui.poketest.rest.berry.get.get_all import get_all_data
from backend.ui.poketest.rest.berry.get.get_by_id import get_by_id_data

blueprint = Blueprint('get_all_berry_stats', __name__)

@blueprint.route('/get-all-berry-stats', methods=['GET'])
@cache.cached(timeout=120)
def get_all_berry_stats():
    berries = get_all_data()

    ids = [berry['url'].split('/').pop() for berry in berries]

    berries_data = []
    for id in ids:
        berry = get_by_id_data(berry_id=id)
        berries_data.append(berry)

    names = [berry['name'] for berry in berries_data]
    growth_times = [berry['growth_time'] for berry in berries_data]
    growth_times_diff = {berry['growth_time'] for berry in berries_data}
    min_growth_time = min(growth_times)
    max_growth_time = max(growth_times)
    median_growth_time = round(statistics.median(growth_times), 2)
    variance_growth_time = round(statistics.variance(growth_times), 2)
    mean_growth_time = round(statistics.mean(growth_times), 2)
    frequency_growth_time = [ { growth: growth_times.count(growth)} for growth in growth_times_diff]

    return {
        "berries_names": names,
        "min_growth_time": min_growth_time,
        "median_growth_time": median_growth_time,
        "max_growth_time": max_growth_time,
        "variance_growth_time": variance_growth_time,
        "mean_growth_time": mean_growth_time,
        "frequency_growth_time": frequency_growth_time,
    }
