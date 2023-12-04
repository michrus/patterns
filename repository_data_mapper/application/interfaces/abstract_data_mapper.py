from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional

from ...domain.entity import Entity
from ...domain.interfaces.generic_entity import GenericEntity


T = TypeVar('T', bound=GenericEntity)

class AbstractDataMapper(ABC, Generic[T]):

    @abstractmethod
    def delete(self, entity: T) -> None:
        pass

    @abstractmethod
    def find(self, entity_id: str) -> Optional[T]:
        pass

    @abstractmethod
    def insert(self, entity: T) -> None:
        pass

    @abstractmethod
    def query(self, criterions: dict[str,str]) -> List[T]:
        pass

    @abstractmethod
    def read_all(self) -> List[T]:
        pass

    @abstractmethod
    def update(self, entity_id: str, entity: Entity) -> None:
        pass
