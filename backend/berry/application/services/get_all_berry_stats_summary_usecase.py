from backend.berry.application.services.get_all_berry_stats_summary_response import GetAllBerryStatsSummaryResponse
from backend.berry.application.services.get_berry_by_id_usecase import GetBerryByIdUseCase
from backend.berry.domain.all_berry_stats import AllBerryStats
from backend.berry.domain.visualization import Visualization
from backend.shared.domain.repository import Repository


class GetAllBerryStatsSummaryUseCase:
    def __init__(self, repository: Repository, visualization: Visualization):
        self.repository = repository
        self.visualization = visualization

    def execute(self):
        berries = self.repository.get_all()
        berries = berries['results']
        berries = [{'name': berry['name'], 'url': f"/berry/get-by-id/{berry['url'].split('/')[-2]}"} for berry in berries]

        ids = [berry['url'].split('/').pop() for berry in berries]

        berries_data = []
        use_case_get_berry_by_id = GetBerryByIdUseCase(repository=self.repository)
        for id in ids:
            berry = use_case_get_berry_by_id.execute(berry_id=id)
            berries_data.append(berry)

        result = AllBerryStats.create_stats(berries = berries_data)
        data_for_chart = AllBerryStats.create_growth_times(data = berries_data)
        chart = self.visualization.generate_chart(data=data_for_chart)

        response = GetAllBerryStatsSummaryResponse(stats=result, chart=chart)
        return response
