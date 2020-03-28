from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'c8;t}K{MsbK)_7['
# 使用 flask_restful 的 Api
api = Api(app)

# Header 加上 Authorization
# 內容為 JWT access_token
jwt = JWT(app, authenticate, identity) # POST /auth

# /item/chair
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

# 使用者註冊
api.add_resource(UserRegister, '/register')

# 防止 import app.py 時 執行 app.run
if __name__ == '__main__':
    app.run(port=5000, debug=True)
