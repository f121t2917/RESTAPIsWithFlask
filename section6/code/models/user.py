import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    # 定義 ORM 欄位
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        # self.id = _id
        self.username = username
        self.password = password
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    # classmethod修飾符對應的函數不需要實例化，不需要self參數，但第一個參數需要是表示自身類的cls參數，
    # 可以來調用類的屬性，類的方法，實例化對像等
    # def find_by_username(self, username):
    @classmethod
    def find_by_username(cls, username): 
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM users WHERE username = ?"
        # # 需有逗號 (username,)
        # result = cursor.execute(query, (username,)) 
        # row = result.fetchone()
        # # if row is not None:
        # if row:
        #     # user = User(row[0], row[1], row[2])
        #     # 一個星號(比如*a)代表 a 是一個 tuple
        #     # 兩個星號(**b)代表一個字典(dict)，就是一個key對應一個value。
        #     user = cls(*row)
        # else:
        #     user = None
        
        # connection.close()
        # return user

        # 使用 SQLAlchemy
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM users WHERE id = ?"
        # # 需有逗號 (username,)
        # result = cursor.execute(query, (_id,)) 
        # row = result.fetchone()
        # # if row is not None:
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        
        # connection.close()
        # return user
        return cls.query.filter_by(id=_id)
