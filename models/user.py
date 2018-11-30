import sqlite3
from db import db

class User(db.Model):
	TABLE_NAME = 'users'
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80))
	password = db.Column(db.String(80))
	
	def __init__(self, _id, username, password):
		self.id = _id
		self.username = username
		self.password = password
	
	@classmethod
	def find_by_username(cls, username):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "SELECT * FROM {table} WHERE username=?".format(table=cls.TABLE_NAME)
		result = cursor.execute(query, (username,))
		row = result.fetchone()
		
		connection.close()
		return cls(*row) if row else None

	@classmethod
	def find_by_id(cls, _id):
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
		result = cursor.execute(query, (_id,))
		row = result.fetchone()
		
		connection.close()
		return cls(*row) if row else None
