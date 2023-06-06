from backend.berry.application.services.get_all_berries_usecase import GetAllBerriesUseCase
from backend.tests.berry.infraestructure.fake_repository import FakeRepository


def test_success_when_get_all_berries():
    repository = FakeRepository()
    use_case = GetAllBerriesUseCase(repository=repository)
    result = use_case.execute()

    assert len(result) == 2