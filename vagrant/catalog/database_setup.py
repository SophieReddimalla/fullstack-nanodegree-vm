import sys

from sqlalchemy import Column, ForeignKey, Integer, String 

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    id = Column(
        Integer, primary_key = True
    )
    description = Column(
        String(50), nullable = False
    )
    created_by = Column(
        Integer, ForeignKey('cat_user.id')
    )
    

class Item(Base):
    __tablename__ = 'item'
    id = Column(
        Integer, primary_key = True
    )
    description = Column(
        String(50), nullable = False
    )
    created_by = Column(
        Integer, ForeignKey('cat_user.id')
    )
    cat_id = Column(
        Integer, ForeignKey('category.id') 
    )

     
class User(Base):
    __tablename__ = 'cat_user'
    id = Column(
        Integer, primary_key = True
    )
    username = Column(
        String(50), nullable = False
    )
    password = Column(
        String(50), nullable = False
    )


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)


   

