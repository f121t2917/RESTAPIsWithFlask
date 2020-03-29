import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
    
    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()

        # if row:
        #     # return {'item': {'name': row[0], 'price': row[1]}}
        #     # 改成返回 ItemModel
        #     # return cls(row[0], row[1])
        #     return cls(*row)

        # 使用 SQLAlchemy
        # return ItemModel.query.filter_by(name=name).filter_by(id=1) # 可以一直 
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name
    
    # @classmethod
    # def insert(cls, item):
    # 改成 update_item.insert() 來新增到資料庫
    # def insert(self):
    def save_to_db(self): # save_to_db 更適合此動作
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO items VALUES (?, ?)"
        # cursor.execute(query, (self.name, self.item))

        # connection.commit()
        # connection.close()

        # 使用 SQLAlchemy
        db.session.add(self)
        db.session.commit()
    
    # @classmethod
    # def update(cls):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "UPDATE items SET price=? WHERE name=?"
        # cursor.execute(query, (self.item, self.item))

        # connection.commit()
        # connection.close()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


