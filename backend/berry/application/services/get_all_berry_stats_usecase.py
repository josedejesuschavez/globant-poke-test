from backend.berry.application.services.get_all_berry_stats_response import GetAllBerryStatsResponse
from backend.berry.application.services.get_berry_by_id_usecase import GetBerryByIdUseCase
from backend.berry.domain.all_berry_stats import AllBerryStats
from backend.berry.domain.visualization import Visualization
from backend.shared.domain.repository import Repository


class GetAllBerryStatsUseCase:
    def __init__(self, repository: Repository):
        self.repository = repository

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

        response = GetAllBerryStatsResponse(
            berries_names=result['berries_names'],
            frequency_growth_time=result['frequency_growth_time'],
            max_growth_time=result['max_growth_time'],
            mean_growth_time=result['mean_growth_time'],
            median_growth_time=result['median_growth_time'],
            min_growth_time=result['min_growth_time'],
            variance_growth_time=result['variance_growth_time'],
        )
        return response
