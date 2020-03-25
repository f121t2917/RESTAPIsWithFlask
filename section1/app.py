# -*- coding: UTF-8 -*-
from flask import Flask, jsonify, request, render_template

# 當 Flask 運行時
# __name__ 為了讓 Flask 知道該應用程序在特定的位置運行
app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ],
    }
]

# route 裝飾器
@app.route('/')
def home():
    # 使用 render_template
    return render_template('index.html')

# POST - used to receive data
# GET - used to send data back only

# 建立商店名稱
# POST /store data:{name:}
@app.route('/store', methods=['POST'])
def create_sotre():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'item': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_sotre(name):
    # Iterate over stores
    # if the store name matches, return it
    # if none match, return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

# GET /store
@app.route('/store')
def get_sotres():
    return jsonify({ 'stores': stores })

# POST /store/<string:name/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    request_data = request.get_json()

    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price'],
            }
            store['item'].append(new_item)
            return jsonify(new_item)

    return jsonify({'message': 'store not found'})

# GET /store/<string:name/item
@app.route('/store/<string:name>/item')
def get_item_in_store():
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    
    return jsonify({'message': 'item not found'})

# python app.py
# 運行 port 5000
app.run(port=5000)