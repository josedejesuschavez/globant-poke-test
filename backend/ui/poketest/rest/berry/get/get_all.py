from flask import Blueprint, render_template
from backend.berry.infraestructure.pokeapi_repository import PokeAPIRepository
from backend.shared.infraestructure.cache import cache

blueprint = Blueprint('get_all_berries', __name__)

@cache.memoize(timeout=120)
def get_all_data():
    repository = PokeAPIRepository()
    berries = repository.get_all()
    berries = berries['results']
    berries = [{'name': berry['name'], 'url': f"/berry/get-by-id/{berry['url'].split('/')[-2]}"} for berry in berries]
    return berries

@blueprint.route('/get-all', methods=['GET'])
@cache.cached(timeout=120)
def get_all():
    berries = get_all_data()
    return render_template('all_berries.html', berries = berries)
