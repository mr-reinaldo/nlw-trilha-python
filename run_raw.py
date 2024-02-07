from barcode import Code128
from barcode.writer import ImageWriter
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/create_tag", methods=["POST"])
def create_tag():
    body = request.json
    product_code = body.get("product_code")

    tag = Code128(product_code, writer=ImageWriter())
    tag.save(f"{tag}")

    return jsonify({"message": f"Tag {tag} created successfully"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
