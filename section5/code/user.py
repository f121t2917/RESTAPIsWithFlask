import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    
    # classmethod修飾符對應的函數不需要實例化，不需要self參數，但第一個參數需要是表示自身類的cls參數，
    # 可以來調用類的屬性，類的方法，實例化對像等
    # def find_by_username(self, username):
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        # 需有逗號 (username,)
        result = cursor.execute(query, (username,)) 
        row = result.fetchone()
        # if row is not None:
        if row:
            # user = User(row[0], row[1], row[2])
            # 一個星號(比如*a)代表 a 是一個 tuple
            # 兩個星號(**b)代表一個字典(dict)，就是一個key對應一個value。
            user = cls(*row)
        else:
            user = None
        
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id = ?"
        # 需有逗號 (username,)
        result = cursor.execute(query, (_id,)) 
        row = result.fetchone()
        # if row is not None:
        if row:
            user = cls(*row)
        else:
            user = None
        
        connection.close()
        return user

class UserRegister(Resource):
    """
    使用者註冊
    """
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User create successfully."}, 201