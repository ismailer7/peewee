from peewee import *


db = SqliteDatabase('test.db')

class BaseModel(Model):

	class Meta:
		database = db



class User(BaseModel):
	user_id = CharField(primary_key=True)
	username = CharField(max_length=25)
	password = CharField(max_length=30)

class Shop(BaseModel):
	shop_id = CharField(primary_key=True)
	shop_name = CharField(max_length=30)

class NearBy(BaseModel):
	user = ForeignKeyField(User)
	shop = ForeignKeyField(Shop)
	class Meta:
		primary_key = CompositeKey('user', 'shop')



def connect():
	db.connect()
	db.create_tables([User, Shop, NearBy], safe=True)


if __name__ == '__main__':
	connect()
	
	User.create(user_id='xxx', username='sma', password='pass1')
	User.create(user_id='yyy', username='kenneth', password='passke')
	User.create(user_id='zzz', username='creg', password='passcreg')

	Shop.create(shop_id='sss', shop_name='shop1')
	Shop.create(shop_id='fff', shop_name='shop2')
	Shop.create(shop_id='ccc', shop_name='shop3')

	NearBy.create(user='xxx', shop='sss')
	NearBy.create(user='xxx', shop='fff')
	NearBy.create(user='zzz', shop='ccc')
	NearBy.create(user='xxx', shop='ccc')
	NearBy.create(user='yyy', shop='sss')
	NearBy.create(user='zzz', shop='fff')
	NearBy.create(user='zzz', shop='sss')
	NearBy.create(user='yyy', shop='fff')

	query = (Shop.select().join(NearBy).join(User).where(User.username=='sma'))
	for shop in query:
		print(shop.shop_name)