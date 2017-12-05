"""
This is Docstring
"""
from flask          import Flask, render_template
from sqlalchemy     import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User


# Create engine and bind to session
engine = create_engine('postgresql+psycopg2:///catalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__,static_url_path='')

@app.route('/')
##Creating category list
def category_list():
    categories = session.query(Category).all()
    return render_template('category_list.html', categories = categories)
##Displaying items for the category 
@app.route('/category/view/<int:category_id>')
def category_view(category_id):
    category = session.query(Category).filter_by(id = category_id).first()
    items = session.query(Item).filter_by(cat_id = category_id)
    return render_template('item_list.html', items = items, category = category)
##Deleting the category
@app.route('/category/delete/<int:category_id>')
def category_delete(category_id):
    category = session.query(Category).filter_by(id = category_id).first()
    category_name = category.description
    items = session.query(Item).filter_by(cat_id = category_id)
    for item in items:
        session.delete(item)
    session.commit()
    session.delete(category)
    session.commit()
    return render_template('category_delete.html', category_name = category_name)

 ##Updating the category
@app.route('/category/update/<int:category_id>')
def category_update(category_id):
    category = session.query(Category).filter_by(id = category_id).first()
    return render_template('category_update.html', category = category)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)