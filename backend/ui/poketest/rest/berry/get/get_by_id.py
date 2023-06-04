from flask import Blueprint, render_template
from backend.berry.infraestructure.pokeapi_repository import PokeAPIRepository
from backend.ui.poketest.cache import cache

blueprint = Blueprint('get_by_id_berry', __name__)

@blueprint.route('/get-by-id/<berry_id>', methods=['GET'])
#@cache.cached(timeout=5)
def get_by_id(berry_id: int):
    repository = PokeAPIRepository()
    berry = repository.get_by_id(id = berry_id)
    return render_template('berry.html', berry=berry)