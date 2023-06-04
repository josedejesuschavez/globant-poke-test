from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def get_all(self, reference):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int):
        raise NotImplementedError