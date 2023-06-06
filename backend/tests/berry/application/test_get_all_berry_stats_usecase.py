from backend.berry.application.services.get_all_berry_stats_response import GetAllBerryStatsResponse
from backend.berry.application.services.get_all_berry_stats_usecase import GetAllBerryStatsUseCase
from backend.tests.berry.infraestructure.fake_repository import FakeRepository


def test_success_when_get_all_berry_stats():
    repository = FakeRepository()
    use_case = GetAllBerryStatsUseCase(repository=repository)
    result = use_case.execute()

    assert result is not None
    assert type(result) == GetAllBerryStatsResponse