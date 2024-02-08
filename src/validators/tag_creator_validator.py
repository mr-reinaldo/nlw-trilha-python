from cerberus import Validator

from src.errors.error_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)


def tag_creator_validator(request: any) -> None:
    body_validato = Validator(
        {"product_code": {"type": "string", "required": True, "empty": False}}
    )

    response = body_validato.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(body_validato.errors)
