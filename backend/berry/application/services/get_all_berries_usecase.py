from backend.berry.application.services.get_all_berries_response import GetAllBerriesResponse
from backend.shared.domain.repository import Repository


class GetAllBerriesUseCase:
    def __init__(self, repository: Repository):
        self.repository = repository

    def execute(self):
        berries = self.repository.get_all()
        berries = berries['results']
        response = [ GetAllBerriesResponse(name=berry['name'], url=f"/berry/get-by-id/{berry['url'].split('/')[-2]}") for berry in berries]
        return response
