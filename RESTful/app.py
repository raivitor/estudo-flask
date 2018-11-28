from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
	def get(self, name):
		for item in items:
			if item['name'] == name:
				return item
		return {'item': None}

api.add_resource(Item, '/item/<string:name>')

app.run(port=5000)
