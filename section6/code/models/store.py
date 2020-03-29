from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    """
    lazy
    select 就是訪問到屬性的時候，就會全部加載該屬性的數據。
    joined 則是在對關聯的兩個表進行join操作，從而獲取到所有相關的對象。
    dynamic 則不一樣，在訪問屬性的時候，並沒有在內存中加載數據，又返回一個query對象，需要執行相應方法 .all() 才可以獲取對象
    """
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()