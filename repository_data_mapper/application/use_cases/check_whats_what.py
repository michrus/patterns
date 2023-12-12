from ..interfaces.abstract_data_mapper import AbstractDataMapper
from ..repositories.entity_repository import GenericRepository
from ...domain.entity import Entity

class CheckWhatsWhatUseCase:
    def __init__(self,
                 presenter,
                 data_mapper: AbstractDataMapper) -> None:
        self._presenter = presenter
        self._data_mapper = data_mapper
        self._entity_repository = \
            GenericRepository[Entity](data_mapper=self._data_mapper)

    def execute(self,
                entity_id: str,
                float_value: float) -> None:
        entity = self._entity_repository.get_by_id(entity_id=entity_id)
        entity.do_business()
        result = entity.check_whats_what(input_float=float_value)
