from flask import Flask, request
from flask_restful import Resource, Api
import get_ingredients as g
import login as l
import socket
import register as r
#import determine as d
import numpy
host = str(socket.gethostbyname(socket.gethostname()))

app = Flask(__name__)
api = Api(app)

todos = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        barcode = request.args.get('img', type=str)
        b = g.Barcode()
        ret = b.barcode(barcode)
        return ret

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
    def login(self, user, pas):
        lo = l.Login()
        ret = lo.login(user,pas)
        return ret


api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True,host=host)
