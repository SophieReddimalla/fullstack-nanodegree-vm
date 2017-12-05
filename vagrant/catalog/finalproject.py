from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def index():
    return 'Index Page'

@app.route('/category/<int:cat_id>')
def showCategory(cat_id):
    #retreive from database the category with id = cat_id
    return render_template('category.html', category=category)

@app.route('/category/create')
def create():
    return 'Create new category'
    #return render_template('newCategory.html', category=category)    
if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
