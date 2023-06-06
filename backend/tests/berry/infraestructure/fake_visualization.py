from backend.berry.domain.visualization import Visualization


class FakeVisualization(Visualization):
    def __init__(self):
        pass

    def generate_chart(self, data) -> str:
        return None
