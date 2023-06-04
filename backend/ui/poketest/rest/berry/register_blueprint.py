from backend.ui.poketest.register_blueprint import RegisterBlueprint
from backend.ui.poketest.rest.berry.get import get_all, get_by_id


class BerryRegisterBlueprint(RegisterBlueprint):
    def __init__(self):
        pass

    def register(self, app):
        app.register_blueprint(get_all.blueprint, url_prefix='/berry')
        app.register_blueprint(get_by_id.blueprint, url_prefix='/berry')
        return app