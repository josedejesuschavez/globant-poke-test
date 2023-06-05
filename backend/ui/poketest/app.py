from flask import Flask

from backend.shared.infraestructure.cache import cache
from backend.ui.poketest.register_modules_blueprint import RegisterModulesBlueprint
from backend.ui.poketest.rest.berry.register_blueprint import BerryRegisterBlueprint

def isinstance_filter(obj, type):
    return isinstance(obj, type)

def create_app():
    app = Flask(__name__)
    register_module = RegisterModulesBlueprint(app)
    register_module.append_module(BerryRegisterBlueprint())
    app = register_module.register()

    cache.init_app(app)

    return app
