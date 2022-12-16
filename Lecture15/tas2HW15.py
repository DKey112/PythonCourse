'''
Используя ORM peewee (https://pypi.org/project/peewee/) создайте функцию которая получает 
от пользователя название альбома через input и выводит список всех треков в этом альбоме
'''
from peewee import *

db = SqliteDatabase('chinook.db')


class BaseModel(Model):
    class Meta:
        database = db


class Albums(BaseModel):
    title = TextField(column_name='Title', null=True)
    albumid = AutoField(column_name='Albumid')

    class Meta:
        table_name = 'albums'


class Tracks(BaseModel):
    name = TextField(column_name='Name', null=True)
    albumid = AutoField(column_name='Albumid')

    class Meta:
        table_name = 'tracks'


def tracks():
    s = input('Choose some album: ')
    with db:
        query = Tracks.select().where(Tracks.albumid == Albums.select().where(Albums.title == s))
        return list(query.dicts())
        

get_t = tracks()

for t in get_t:
    print(t)
