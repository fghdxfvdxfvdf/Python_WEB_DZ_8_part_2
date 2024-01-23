from mongoengine import *


password = '2zNCrgJpCMgtZivG'
user = 'aaa1113341998825'
db = 'hw_8_redis'

connect(host='mongodb+srv://aaa1113341998825:2zNCrgJpCMgtZivG@cluster0.ylqzlor.mongodb.net/', db=db)


class User(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    address = StringField()