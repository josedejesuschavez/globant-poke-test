import base64
import io
import statistics
from flask import Blueprint, render_template
import matplotlib.pyplot as plt
from backend.ui.poketest.cache import cache
from backend.ui.poketest.rest.berry.get.get_all import get_all_data
from backend.ui.poketest.rest.berry.get.get_by_id import get_by_id_data


blueprint = Blueprint('get_all_berry_stats', __name__)

@cache.memoize(timeout=120)
def get_all_berry_stats_data():
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
    frequency_growth_time = [{growth: growth_times.count(growth)} for growth in growth_times_diff]

    return growth_times, {
        "berries_names": names,
        "min_growth_time": min_growth_time,
        "median_growth_time": median_growth_time,
        "max_growth_time": max_growth_time,
        "variance_growth_time": variance_growth_time,
        "mean_growth_time": mean_growth_time,
        "frequency_growth_time": frequency_growth_time,
    }

def generate_histogram(data):
    hist, bins, _ = plt.hist(data, bins=30, edgecolor='black', rwidth=0.8)

    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.xticks(range(min(data), max(data)))

    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)

    img_base64 = base64.b64encode(img_bytes.read()).decode('ascii')

    plot_html = '<img style="margin: 0 auto; display: block;" src="data:image/png;base64,{}">'.format(img_base64)

    return plot_html

@blueprint.route('/allBerryStats', methods=['GET'])
@cache.cached(timeout=120)
def get_all_berry_stats():
    _, data = get_all_berry_stats_data()
    return data


@blueprint.route('/allBerryStatsSummary', methods=['GET'])
@cache.cached(timeout=120)
def get_all_berry_stats_summary():
    growth_times, data = get_all_berry_stats_data()
    plot_html = generate_histogram(data=growth_times)
    return render_template('all_berry_stats_summary.html', plot=plot_html, data=data)
