from src.controllers.tag_creator_controller import TagCreatorController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreatorView:

    def validato_and_create(self, http_request: HttpRequest):
        tag_creator_controller = TagCreatorController()

        body = http_request.body
        product_code = body["product_code"]

        # Logica de regra de negocio
        response = tag_creator_controller.create(product_code)

        # retorno http
        return HttpResponse(
            status_code=200,
            body=response,
        )
