from flask import Flask

from backend.ui.poketest.register_modules_blueprint import RegisterModulesBlueprint
from backend.ui.poketest.rest.berry.register_blueprint import BerryRegisterBlueprint


def create_app():
    app = Flask(__name__)
    register_module = RegisterModulesBlueprint(app)
    register_module.append_module(BerryRegisterBlueprint())
    app = register_module.register()
    return app
