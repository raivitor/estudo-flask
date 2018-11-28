from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
	def get(self, name):
		# Usei uma lambda function para verificar se o nome recebido existe.
		# Vai ser retornado um filter object pelo filter, então usei o next para pegar
		# o primeiro valor e caso não exista nenhum valor, este será None
		item = next(filter(lambda x: x['name'] == name, items), None)
		return {'item': None}, 200 if item else 404

	def post(self, name):
		if next(filter(lambda x: x['name'] == name, items), None):
			return {'message': "An item with name '{}' already exist.".format(name)}, 400

		data = requeste.get_json()
		item = {'name': name, 'price': data['price']}
		items.append(item)
		return item, 201


class ItemList(Resource):
	def get(self):
		return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000)
