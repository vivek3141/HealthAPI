from flask import Flask, request
import get_ingredients as g

app = Flask(__name__)


@app.route("/")
def get(self):
    barcode = request.args.get('barcode', type=str)
    b = g.Barcode()
    ret = b.barcode(barcode)
    return ret

