from flask import Blueprint, render_template, json
from backend.berry.application.services.get_berry_by_id_usecase import GetBerryByIdUseCase
from backend.berry.infraestructure.pokeapi_repository import PokeAPIRepository
from backend.shared.infraestructure.cache import cache


blueprint = Blueprint('get_by_id_berry', __name__)

@blueprint.route('/get-by-id/<berry_id>', methods=['GET'])
@cache.cached(timeout=120)
def get_by_id(berry_id: int):
    use_case = GetBerryByIdUseCase(repository=PokeAPIRepository())

    result = use_case.execute(berry_id=berry_id)
    return render_template('berry.html', berry=result)