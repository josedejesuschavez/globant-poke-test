from backend.berry.application.services.get_berry_by_id_response import GetBerryByIdResponse
from backend.berry.application.services.get_berry_by_id_usecase import GetBerryByIdUseCase
from backend.tests.berry.infraestructure.fake_repository import FakeRepository


def test_success_when_get_berry_by_id():
    repository = FakeRepository()
    use_case = GetBerryByIdUseCase(repository=repository)
    result = use_case.execute(berry_id=1)

    assert result is not None
    assert type(result) == GetBerryByIdResponse
