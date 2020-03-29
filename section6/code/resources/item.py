import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

# 定義 class
class Item(Resource):
    # 請求解析
    parser = reqparse.RequestParser()

    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    parser.add_argument('sotre_id',
        type=float,
        required=True,
        help="Every item needs a store id"
    )

    # 也可以使用裝飾器 但如果 class 分散會不好管理
    #@app.route('/item/<string:name')
    # 加入 jwt 裝飾器，訪問時需要有 access_token 才能訪問
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()

        return {'message': 'Item not found'}, 404
    
    def post(self, name):
        # 如果回傳不是 None 則回傳已存在
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()
        # item = {'name': name, 'price': data['price']}
        # item = ItemModel(name, data['price'], data['store_id'])
        item = ItemModel(**data)

        try:
            # ItemModel.insert(item)
            # item.insert()
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201
    
    def delete(self, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "DELETE FROM items WHERE name=?"
        # cursor.execute(query, (name,))

        # connection.commit()
        # connection.close()

        item = Item.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        # updated_item = {'name': name, 'price': data['price']}
        updated_item = ItemModel(name, data['price'], data['store_id'])

        if item is None: # 不存在則新增
            # try:
            #     # self.insert(updated_item)
            #     updated_item.insert()
            # except:
            #     return {"message": "An error occurred inserting the item."}, 500
            # item = ItemModel(name, data['price'], data['store_id'])
            item = ItemModel(name, **data)
        else:
            # try:
            #     # self.update(updated_item) # 存在則更新資料
            #     updated_item.update() # 存在則更新資料
            # except:
            #     return {"message": "An error occurred updating the item."}, 500
            item.price = data['price']
        
        item.save_to_db()

        return updated_item.json()

class ItemList(Resource):
    def get(self):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items"
        # result = cursor.execute(query)

        # items = []
        # for row in result:
        #     items.append({'name': row[0], 'price': row[1]})

        # connection.close()

        # return {'items': items}
        # 返回 json
        return {'items': [item.json() for item in ItemModel.query.all()]}
        # 使用 lambda
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
