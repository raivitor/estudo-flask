# coding: utf-8
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

stores = [{
    'name': 'My Store',
    'items': [{'name':'my item', 'price': 15.99 }]
}]


@app.route("/")
def home():
    return render_template("index.html", myname="Rai"), 200

@app.route("/get")
def get():
	return render_template("get.html"), 200

@app.route("/post")
def post():
	return render_template("post.html"), 200

@app.route("/receive/", methods=['GET','POST'])
def receive():
	if request.method == "GET":
		return u"Type GET!<br>name: {} <br>age: {}".format(request.args.get("name"),request.args.get("age")), 200
	elif request.method == "POST":
		return u"Type POST!<br>name: {} <br>age: {}".format(request.form["name"],request.form["age"]), 200


@app.route("/info")
@app.route("/info/<name>")
@app.route("/info/<name>/<age>")
def info(name = None, age = None):
	return u"Name: {}<br>Age: {}".format(name, age), 200

#get /store
@app.route('/store')
def get_stores():
  return jsonify({'stores': stores})

#post /store data: {name :}
@app.route('/store' , methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name':request_data['name'],
    'items':[]
  }
  stores.append(new_store)
  return jsonify(new_store)

#get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
  for store in stores:
    if store['name'] == name:
          return jsonify(store)
  return jsonify ({'message': 'store not found'})

#post /store/<name> data: {name :}
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
  request_data = request.get_json()
  for store in stores:
    if store['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'store not found'})

#get /store/<name>/item data: {name :}
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
  for store in stores:
    if store['name'] == name:
        return jsonify( {'items':store['items'] } )
  return jsonify ({'message':'store not found'})

app.run(port=5000)