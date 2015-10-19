# -*- coding: utf-8 -*-

'''
# Sqlite3例子
import sqlite3
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) PRIMARY KEY, name varchar(20))')
cursor.execute('INSERT INTO user (id, name) values (\'1\', \'Michael\')')
cursor.rowcount
cursor.close()
conn.commit()
conn.close()
'''

'''
# MySql例子
import mysql.connector
conn = mysql.connector.connect(user='root', password='tayasql', database='test', use_unicode=True)
cursor = conn.cursor()

# cursor.execute('create TABLE user (id varchar(20) PRIMARY KEY, name varchar(20))')
# cursor.execute('insert INTO user (id, name) values (%s, %s)', ['2', 'taya'])
# cursor.rowcount

# conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user')
# cursor.execute('select * from user where id=1')
# 注意execute的附加参数，必须是tuple对象
# cursor.execute('select * from user WHERE id = %s', ('1',))
# 返回tuple对象
values = cursor.fetchall()
print values

cursor.close()
conn.close()
'''

# SqlAlchemy例子

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # books = relationship('Book')


class School(Base):
    __tablename__ = 'school'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # user_id = Column(String(20), ForeignKey('user.id'))

engine = create_engine('mysql+mysqlconnector://root:tayasql@localhost:3306/test2', echo=True)

# create tables!!!
Base.metadata.create_all(engine)

DBsession = sessionmaker(bind=engine)
session = DBsession()

new_user = User(id='5', name='Bob')
new_book = Book(id='1', name='HarryPotter')

session.add(new_user)
# session.flush()
session.commit()
session.close()

