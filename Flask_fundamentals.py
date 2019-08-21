
#!/usr/bin/python
# C:\python\python\MyFirstFlaskApi\MyFirstApiPython.py
"""
    Purpose: Books Api
"""
from flask import Flask, jsonify,request,Response
import random
import requests
from books_validator import validate_book
import json

app = Flask(__name__)
print(__name__)

books = [
    {
        'name': 'The GrassHopper',
        'price': 123,
        'isbn': 23452345234
    },
    {
        'name': 'The wings of the fire',
        'price': 23.5,
        'isbn': 23452345
    }
]
# Get Books
@app.route('/books')
def get_books():
    return jsonify({'books': books})

@app.route('/books/<int:isbn>')
def find_books_by_isbn(isbn):
    for book in books:
        if book['isbn']==isbn:
            return jsonify({
                'name':book['name'],
                'price':book['price']
            })

@app.route('/books',methods=['POST'])
def add_book():
    book_to_store = request.get_json()
    if(validate_book(book_to_store)):
        validated_book = {
            "name":book_to_store["name"],
            "price":book_to_store["price"],
            "isbn":book_to_store["isbn"]
        }
        books.insert(0,validated_book)
        response = Response("",201,mimetype="application/json")
        response.headers["Location"]="/books/"+str(book_to_store['isbn'])
        return response
    else:
        _body = {
            'error':'The format of book is not proper',
            "helpstring":'please passs in the format likename: <BOOKNAME>,price: <Price>,Isbn: <Isbn>'
        }
        response = Response(json.dumps( _body),400,mimetype="application/json")
        return response


@app.route('/possibility/<int:userinput>')
def get_possibilities(userinput):
        return jsonify({'possibilities' : [ "Heads" if not random.randint(0,1) else "Tails" for x in range(userinput) ]})



app.run(port=5000,debug=True)
