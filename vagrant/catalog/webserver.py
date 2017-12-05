from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

## Imported CRUD operations 
from database_setup import Base, Category, Item, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

##Create session and connect to DB
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
session = DBSession()
DBSession = sessionmaker(bind=engine)


class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            ## To Create a new category
            if self.path.endswith("/category/new"):
                self.send_response(200)
                self.send_header('Content-type',    'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1> Make A new Category </h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='/category/new'>"
                output += "<input name='newCategoryName' type='text' placeholder = 'New Category Name'>"
                output += "<input type= 'submit' value='Create'>"
                output += "</html></body>"
                self.wfile.write(output)
                return



            if self.path.endswith("/category"):
                Category = session.query(category).all()
                output = ""
                output += "<a href = '/category/new'>Make a New Category Here </a></br></br>"
                self.send_response(200)
                self.send_header('Content-type',    'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                for category in Category:
                    output += category.description 
                    output += "</br>"
                    output += "<a href = '/category/%s/edit' >Edit</a>" % category.id
                    output += "</br>"
                    output += "<a href = '/category/%s/delete'>Delete</a> " % category.id
                    output += "</br>"

                output += "</body></html>"
                self.wfile.write(output)
                return     
            

            ## Delete Option in category
            if  self.path.endswith("/delete"):

                categoryIDPath = self.path.split("/")[2]

                myCategoryQuery = session.query(category).filter_by(id = categoryIDPath).one()
                if myCategoryQuery != [] :
                    self.send_response(200)
                    self.send_header('Content-type',    'text/html')
                    self.end_headers()
                    output = ""
                    output = "<html><body>"
                    output = "<h1>Are you sure you want to delete %s?" % myCategoryQuery.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/category/%s/delete'>" % categoryIDPath
                    output += "<input type= 'submit' value='Delete'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output) 

  
            ## Testing Hello
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Hello!</body></html>"
                output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'></form>
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)    
   
    def do_POST(self)
    try:
        # Delete category form
        if self.path.endswith("/delete"):

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

            categoryIDPath = self.path.split("/")[2]

            myCategoryQuery = session.query(category).filter_by(id = categoryIDPath).one()

            if myCategoryQuery != []:
                session.delete(myCategoryQuery)
                session.commit()
                self.send_response(301)
                self.send_header('Content-type',    'text/html')
                self.send_header('Location','/category')
                self.end_headers()

        
         ## Edit option in category
        if self.path.endswith("/edit"):
            categoryIDPath = self.path.split("/")[2]

             myCategoryQuery = session.query(Category).filter_by(id = categoryIDPath).one()

              if myCategoryQuery != [] :
                    myCategoryQuery.name = messagecontent[0]
                    session.add(myCategoryQuery)
                    session.commit()
                    self.send_response(301)
                    self.send_header('Content-type',   'text/html')
                    self.send_header('Location', '/category')


        if self.path.endswith("/category/new"):
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields=cgi.parse_multipart(self.rfile, pdict)
            messagecontent = fields.get('newCategoryName')


            #Create new Class
            newCategory = Category(name = messagecontent[0])
            session.add(newCategory)
            session.commit()

            self.send_response(301)
            self.send_header('Content-type',    'text/html')
            self.send_header('Location', '/category')
            self.end_headers()

            return    




        self.send_response(301)
        self.end_headers()
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            fields=cgi.parse_multipart(self.rfile, pdict)
            messagecontent = fields.get('message')

        output = ""
        output += "<html><body>"
        output += "<h2> Okay, how about this: </h2>"
        output += "<h1> %s </h1>" % messagecontent[0]    
        output += "<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name='message' type='text'><input type='submit' value='Submit'></form>
        output += "</body></html>"
        self.wfile.write(output)
        print output
        
    except:
        pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print "Web server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()

