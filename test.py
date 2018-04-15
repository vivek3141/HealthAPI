from flask import Flask, request
from flask_restful import Resource, Api
import get_ingredients as g

app = Flask(__name__)
api = Api(app)

barcodes = {}

class Health(Resource):
    def get(self, data_id):
        b = g.Barcode()
        ret = b.barcode(barcodes[data_id])
        return ret

    def put(self, data_id):
        barcodes[data_id] = request.form['data']
        return {data_id: barcodes[data_id]}

api.add_resource(Health, '/<string:data_id>')

if __name__ == '__main__':
    app.run(debug=True)