import sqlite3
from flask import jsonify
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.item import ItemModel

class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument(
    'price',
    type=float,
    required=True,
    help="This field cannot be blank!")

	@jwt_required()
	def get(self, name):
		item = ItemModel.find_by_name(name)
		if item:
				return item.json()
		return {'message': 'Item not found'}, 404

	def post(self, name):
		if ItemModel.find_by_name(name):
			return {'message': "An item with name '{}' already exists.".format(name)}

		data = Item.parser.parse_args()

		item = ItemModel(name, data['price'])

		try:
			item.insert()
		except:
			return {"message": "An error occurred inserting the item."}

		return item.json()

	def delete(self, name):
		if not ItemModel.find_by_name(name):
			return {'message': 'Item not found'}, 404

		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "DELETE FROM {table} WHERE name=?".format(table=ItemModel.TABLE_NAME)
		cursor.execute(query, (name,))

		connection.commit()
		connection.close()

		return {'message': 'Item deleted'}

	def put(self, name):
		data = Item.parser.parse_args()
		item = ItemModel.find_by_name(name)
		updated_item = ItemModel(name, data['price'])
		if item:
			try:
				updated_item.update()
			except:
				return {"message": "An error occurred updating the item."}, 500
		else:
			return {'message': 'Item not found'}, 404
		return updated_item.json()


class ItemList(Resource):
	TABLE_NAME = 'items'

	def get(self):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "SELECT * FROM {table}".format(table=ItemModel.TABLE_NAME)
		result = cursor.execute(query).fetchall()
		connection.close()

		return jsonify({'items': result})