from flask import Blueprint, render_template, jsonify

from backend.berry.application.services.get_all_berry_stats_summary_usecase import GetAllBerryStatsSummaryUseCase
from backend.berry.application.services.get_all_berry_stats_usecase import GetAllBerryStatsUseCase
from backend.berry.infraestructure.matplotlib_visualization import MatplotlibVisualization
from backend.berry.infraestructure.pokeapi_repository import PokeAPIRepository
from backend.shared.infraestructure.cache import cache


blueprint = Blueprint('get_all_berry_stats', __name__)

@blueprint.route('/allBerryStats', methods=['GET'])
@cache.cached(timeout=120)
def get_all_berry_stats():
    use_case = GetAllBerryStatsUseCase(repository=PokeAPIRepository())
    result = use_case.execute()
    return jsonify(result)


@blueprint.route('/allBerryStatsSummary', methods=['GET'])
@cache.cached(timeout=120)
def get_all_berry_stats_summary():
    use_case = GetAllBerryStatsSummaryUseCase(repository=PokeAPIRepository(), visualization=MatplotlibVisualization())
    result = use_case.execute()
    return render_template('all_berry_stats_summary.html', chart=result.chart, data=result.stats)
