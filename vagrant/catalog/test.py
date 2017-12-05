from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def HelloWorld():
    return 'HelloWorld'

@app.route('/hello/create')
def create():
    return 'Create category'

@app.route('/hello/edit')
def edit():
    return 'Edit category'

@app.route('/hello/delete')
def delete():
    return 'Delete category'

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)


    ####
##TO CREATE ,EDIT AND DELETE A CATEGORY
@app.route('/category')
def showCategory():
    return 'category page'
    #return render_template('category.html', category=category)

@app.route('/category/create')
def create():
    return 'Create new category'
    #return render_template('newCategory.html', category=category)


@app.route('/category/edit/<int:cat_id>')
def edit(cat_id):
    return'Edit a category'
    #return render_template('editCategory.html', category=category)

@app.route('/category/delete/<int:cat_id>')
def delete(cat_id):
    return 'Delete a category'
    #return render_template('deleteCategory.html', category=category)
##TO CREATE, EDIT, AND DELETE AN ITEM
@app.route('/item')
def showItem():
    return 'items page'
    #return render_template('item.html', item=item)

@app.route('/item/create')
def create():
    return 'Create new item'
    #return render_template('newItem.html', item=item)

@app.route('/item/edit/<int:cat_id>')
def edit(item_id):
    return'Edit a item'
    #return render_template('editItem.html', item=item)

@app.route('/item/delete/<int:cat_id>')
def delete(item_id):
    return 'Delete a item'
    #return render_template('deleteItem.html', item=item)

