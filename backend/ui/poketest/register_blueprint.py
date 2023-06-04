from abc import ABC, abstractmethod


class RegisterBlueprint(ABC):
    @abstractmethod
    def register(self, app):
        pass
