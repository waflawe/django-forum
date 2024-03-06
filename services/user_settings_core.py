from typing import NamedTuple, Type, Optional

E = int
ErrorMessage = str


class Field(NamedTuple):
    """
    Информация о названии настройки.
    """

    field: str


class Error(NamedTuple):
    """ Информация о коде ошибки, связанной с конкретной настройкой, и ее (ошибки) сообщении об ошибке. """

    error_code: E
    error_message: Optional[ErrorMessage] = None


class ValidationClasses(NamedTuple):
    """ Информация о классах-валидаторах данной настройки на WEB'e и API. """

    web_validation_class: Type
    api_validation_class: Type


class Handler(NamedTuple):
    """ Информация об обработчике настройки. """

    handler: Type
    validation_classes: Optional[ValidationClasses] = None


class Setting(NamedTuple):
    """ Класс настройки. """

    field: Field
    error: Error
    handler: Handler

    def __str__(self):
        return f"{self.field.field.capitalize()} field with {self.handler.handler.handle} handler"


def include_setting(*args, **kwargs) -> Setting:
    return Setting(
        Field(kwargs["field"]),
        Error(E(kwargs["error_code"]), kwargs.get("error_message", None)),
        Handler(kwargs["handler"], kwargs.get("validation_classes", None))
    )
