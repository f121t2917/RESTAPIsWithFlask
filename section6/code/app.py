from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# 如果設置成True (默認情況)，Flask-SQLAlchemy 將會追踪對象的修改並且發送信號。這需要額外的內存， 如果不必要的可以禁用它
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'c8;t}K{MsbK)_7['
# 使用 flask_restful 的 Api
api = Api(app)

"""
如果有多個before_request的時候，只要中間有執行return的部份，後續就不再被執行。

before_first_request
    註冊一個函數，在處理第一個請求之前執行
before_request
    註冊一個函數，在每次請求之前執行
after_request
    註冊一個函數，如果沒有未處理的異常拋出，在每次請求之後執行
teardown_request
    註冊一個函數，如果有未處理的異常拋出，在每次請求之後執行
"""
@app.before_first_request
def create_tables():
    db.create_all()

@app.errorhandler(404)
def error_404(e):
    return '404 Error', 404

# @app.errorhandler(Exception)
# def all_exception_handler(e):
#     return 'Error', 500
@app.errorhandler(Exception)
def all_exception_handler(e):
    # 對於 HTTP 異常，返回自帶的錯誤描述和狀態碼
    # 這些異常類在 Werkzeug 中定義，均繼承 HTTPException 類
    if isinstance(e, HTTPException):
        return e.desciption, e.code
    return 'Error', 500 

# Header 加上 Authorization
# 內容為 JWT access_token
jwt = JWT(app, authenticate, identity) # POST /auth

# /item/chair
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
# 使用者註冊
api.add_resource(UserRegister, '/register')

# 防止 import app.py 時 執行 app.run
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
