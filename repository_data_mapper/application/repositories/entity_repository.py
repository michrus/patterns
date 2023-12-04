from typing import TypeVar, Generic, List, Optional

from ...domain.interfaces.generic_entity import GenericEntity
from ..interfaces.abstract_data_mapper import AbstractDataMapper


T = TypeVar('T', bound=GenericEntity)

class GenericRepository(Generic[T]):
    def __init__(self, data_mapper: AbstractDataMapper[T]) -> None:
        self._data_mapper = data_mapper

    def add(self, entity: T) -> None:
        self._data_mapper.insert(entity)

    def delete(self, entity_id: str) -> None:
        self._data_mapper.delete(entity_id)

    def get_by_id(self, entity_id: str) -> Optional[T]:
        return self._data_mapper.find(entity_id)

    def get_all(self) -> List[T]:
        return self._data_mapper.read_all()

    def update(self, entity_id: str, new_entity: T) -> None:
        self._data_mapper.update(entity_id, new_entity)
