
class GenericEntity:
    def __init__(self, entity_id: str) -> None:
        self._entity_id: str = entity_id

    @property
    def entity_id(self) -> str:
        return self._entity_id
