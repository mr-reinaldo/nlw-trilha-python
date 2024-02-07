from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreatorView:

    def validato_and_create(self, http_request: HttpRequest):
        body = http_request.body
        product_code = body["product_code"]

        # Logica de regra de negocio

        # retorno http
        return HttpResponse(
            status_code=200,
            body={"message": f"Tag {product_code} created successfully"},
        )
