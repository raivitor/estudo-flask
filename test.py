import requests
import unittest
import sqlite3

class TestAPI(unittest.TestCase):
  def setUp(self):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users")
    cursor.execute("DELETE FROM items")
    connection.commit()
    connection.close()

  def test_createUser(self):
    resp = requests.post(
      'http://localhost:5000/register', 
      data={'username': 'raivitor12', 'password': '123123'})
    self.assertEqual(201, resp.status_code)

  # corrigir teste
  def test_auth(self):
    resp = requests.post(
      'http://localhost:5000/auth', 
      data={'username': 'raivitor12', 'password': '123123'})
    self.assertEqual(200, resp.status_code)