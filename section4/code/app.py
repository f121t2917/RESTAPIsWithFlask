from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
# 使用 flask_restful 的 Api
api = Api(app)

# app 重啟前 資料會一直存在
items = []
# 定義 class
class Item(Resource):
    # 請求解析
    parser = reqparse.RequestParser()

    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    # 也可以使用裝飾器 但如果 class 分散會不好管理
    #@app.route('/item/<string:name')
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        # return {'item': None}, 404

        # 使用 filter() 會返回 filter 物件，使用 list() 轉為 list
        # 或使用 next() 返回第一個項目，否則回傳 None
        item = next(filter(lambda x: x['name'] == name, items), None)
        # 如果 item is not None 則 回傳 200，否則 404
        # return {'item': item}, 200 if item is not None else 404

        # 使用 None 如果變數是LIST的話，需注意是 空LIST 還是 None
        return {'item': item}, 200 if item else 404

    def post(self, name):
        # 如果回傳不是 None 則回傳已存在
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        # force = True 為 不需要 content-type，只會查看內容並將格式化
        # data = request.get_json(force=True)

        # silent = True 為 不確定 也不給出錯誤 
        # data = request.get_json(silent=True)
        # data = request.get_json()

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        # 201 created
        # 202 接受了創建了一個對象，但需要很長的時間且不一定成功
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        # Once again, print something not in the args to verify everything works
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

# /item/chair
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
