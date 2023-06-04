class RegisterModulesBlueprint:
    def __init__(self, app):
        self.app = app
        self.modules_blueprints = []

    def append_module(self, module_blueprint):
        self.modules_blueprints.append(module_blueprint)

    def register(self):
        for module in self.modules_blueprints:
            self.app = module.register(self.app)

        return self.app