from dataclasses import dataclass

from backend.berry.application.services.get_berry_by_id_response import GetBerryByIdResponse


@dataclass
class GetAllBerryStatsSummaryResponse:
    stats: GetBerryByIdResponse
    chart: str