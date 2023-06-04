from flask import Blueprint, render_template
from backend.berry.infraestructure.pokeapi_repository import PokeAPIRepository
from backend.ui.poketest.cache import cache

blueprint = Blueprint('get_by_id_berry', __name__)

#@cache.cached(timeout=120)
def get_by_id_data(berry_id: int):
    repository = PokeAPIRepository()
    berry = repository.get_by_id(id=berry_id)
    return berry

@blueprint.route('/get-by-id/<berry_id>', methods=['GET'])
def get_by_id(berry_id: int):
    berry = get_by_id_data(berry_id=berry_id)
    return render_template('berry.html', berry=berry)