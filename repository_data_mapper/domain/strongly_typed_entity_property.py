from .interfaces.generic_entity import GenericEntity


class StronglyTypedEntityProperty(GenericEntity):
    def __init__(self, entity_id: str, prop: dict[str,str]) -> None:
        self._entity_id: str = entity_id
        self._prop: dict[str,str] = prop

    @property
    def entity_id(self) -> str:
        return self._entity_id

    def do_property_stuff(self) -> None:
        print("Just property things...")

    def check_prop(self, key: str) -> bool:
        return key in self._prop
