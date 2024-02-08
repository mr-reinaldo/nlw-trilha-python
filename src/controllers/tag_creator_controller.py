from typing import Dict

from src.drivers.barcode_handler import BarcodeHandler


class TagCreatorController:
    """
    Responsable for implementing business logic to create a tag
    """

    def create(self, product_code: str) -> Dict:
        path_from_tag = self.__create_tag(product_code)
        response = self.__formatted_response(product_code, path_from_tag)

        return response

    def __create_tag(self, product_code: str) -> str:
        barcode_handler = BarcodeHandler()
        path_from_tag = barcode_handler.create_barcode(product_code)

        return path_from_tag

    def __formatted_response(self, product_code: str, path_from_tag: str) -> Dict:
        return {
            "data": {
                "type": "tags",
                "count": 1,
                "path": f"{path_from_tag}.png",
                "attributes": {
                    "product_code": product_code,
                },
            }
        }
