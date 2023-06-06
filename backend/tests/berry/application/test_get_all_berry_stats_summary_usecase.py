from backend.berry.application.services.get_all_berry_stats_summary_response import GetAllBerryStatsSummaryResponse
from backend.berry.application.services.get_all_berry_stats_summary_usecase import GetAllBerryStatsSummaryUseCase
from backend.tests.berry.infraestructure.fake_repository import FakeRepository
from backend.tests.berry.infraestructure.fake_visualization import FakeVisualization


def test_success_when_get_all_berry_stats_summary():
    repository = FakeRepository()
    visualization = FakeVisualization()
    use_case = GetAllBerryStatsSummaryUseCase(repository=repository, visualization=visualization)
    result = use_case.execute()

    assert result is not None
    assert type(result) == GetAllBerryStatsSummaryResponse