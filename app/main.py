from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.book import Book, Books

app = Flask(__name__)
app.secret_key = "you will never gi ss password"
CORS(app)

api = Api(app)


api.add_resource(Books, '/books')
api.add_resource(Book, '/book', '/book/<int:id>',  endpoint="book")




if __name__ == "__main__":
    app.run(port=5000, debug=True)