from backend.berry.application.services.get_berry_by_id_response import GetBerryByIdResponse
from backend.shared.domain.repository import Repository


class GetBerryByIdUseCase:
    def __init__(self, repository: Repository):
        self.repository = repository

    def execute(self, berry_id: int):
        result = self.repository.get_by_id(id=berry_id)
        return GetBerryByIdResponse(
            firmness=result['firmness'],
            flavors=result['flavors'],
            growth_time=result['growth_time'],
            id=result['id'],
            item=result['item'],
            max_harvest=result['max_harvest'],
            name=result['name'],
            natural_gift_power=result['natural_gift_power'],
            natural_gift_type=result['natural_gift_type'],
            size=result['size'],
            smoothness=result['smoothness'],
            soil_dryness=result['soil_dryness'],
        )
