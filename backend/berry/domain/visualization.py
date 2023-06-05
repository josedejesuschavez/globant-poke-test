from abc import ABC, abstractmethod


class Visualization(ABC):

    @abstractmethod
    def generate_chart(self, data) -> str:
        pass