from datetime import datetime

from .interfaces.generic_entity import GenericEntity
from .strongly_typed_entity_property import StronglyTypedEntityProperty


class Entity(GenericEntity):
    def __init__(self,
                 entity_id: str,
                 string_value: str,
                 numeric_value: int,
                 float_value: float,
                 datetime_Value: datetime,
                 entity_property: StronglyTypedEntityProperty) -> None:
        super().__init__(entity_id=entity_id)
        self._string_value: str = string_value
        self._numeric_value: int = numeric_value
        self._float_value: float = float_value
        self._datetime_Value: datetime = datetime_Value
        if entity_property.entity_id == self._entity_id:
            self._entity_property: StronglyTypedEntityProperty = entity_property
        else:
            message = "Entity ID on Entity and EntityProperty do not match!"
            raise EntityError(message)

    @property
    def entity_property(self):
        return self._entity_property

    def do_business(self, business_number: float) -> None:
        print(f"Doing big business with {business_number}")

    def check_whats_what(self, input_float: float) -> bool:
        return input_float > self._float_value


class EntityError(Exception):
    pass
