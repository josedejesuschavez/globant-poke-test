import base64
import io

import matplotlib.pyplot as plt
from backend.berry.domain.visualization import Visualization


class MatplotlibVisualization(Visualization):
    def __init__(self):
        pass

    def generate_chart(self, data) -> str:
        hist, bins, _ = plt.hist(data, bins=30, edgecolor='black', rwidth=0.8)

        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Histogram')
        plt.xticks(range(min(data), max(data)))

        img_bytes = io.BytesIO()
        plt.savefig(img_bytes, format='png')
        img_bytes.seek(0)

        img_base64 = base64.b64encode(img_bytes.read()).decode('ascii')

        plot_html = '<img style="margin: 0 auto; display: block;" src="data:image/png;base64,{}">'.format(img_base64)

        return plot_html
