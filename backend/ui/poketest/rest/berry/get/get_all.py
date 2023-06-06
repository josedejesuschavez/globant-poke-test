from flask import Blueprint, render_template

from backend.berry.application.services.get_all_berries_usecase import GetAllBerriesUseCase
from backend.berry.infraestructure.pokeapi_repository import PokeAPIRepository
from backend.shared.infraestructure.cache import cache

blueprint = Blueprint('get_all_berries', __name__)

@blueprint.route('/get-all', methods=['GET'])
@cache.cached(timeout=120)
def get_all():
    use_case = GetAllBerriesUseCase(repository=PokeAPIRepository())
    response = use_case.execute()
    return render_template('all_berries.html', berries = response)
