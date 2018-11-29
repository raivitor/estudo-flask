from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument(
    'price',
    type=float,
    required=True,
    help="This field cannot be blank!")

	@jwt_required()
	def get(self, name):
		# Usei uma lambda function para verificar se o nome recebido existe.
		# Vai ser retornado um filter object pelo filter, então usei o next para pegar
		# o primeiro valor e caso não exista nenhum valor, este será None
		item = next(filter(lambda x: x['name'] == name, items), None)
		return {'item': item}, 200 if item else 404

	def post(self, name):
		if next(filter(lambda x: x['name'] == name, items), None):
			return {'message': "An item with name '{}' already exist.".format(name)}, 400

		data = Item.parser.parse_args()
		item = {'name': name, 'price': data['price']}
		items.append(item)
		return item, 201

	def delete(self, name):
		global items
		items = list(filter(lambda x: x['name'] != name, items))
		return {'message': 'Item deleted'}

	def put(self, name):
		data = Item.parser.parse_args()
		item = next(filter(lambda x: x['name'] == name, items), None)
		if item is None:
			item = {'name': name, 'price': data['price']}
			items.append(item)
		else:
			item.update(data)
		return item


class ItemList(Resource):
	def get(self):
		return {'items': items}
