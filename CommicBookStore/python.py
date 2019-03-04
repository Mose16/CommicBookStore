from bottle import run, route, view, get, post, request, static_file
from itertools import count


class User:
    books_in_cart = []
    name = None
    
    def __init__(self, name):
        self.name = name
    
    
class Book:
    _ids = count (0)
    name = "How the heck would I know"
    description = "It seems no one cared enough to write a description."
    cost = "At least $0"
    stock = "Probably none"
    photo = "Void"
    
    def __init__(self, 
                 name = "How the heck would I know",
                 description = "It seems no one cared enough to write a description.",
                 cost = "At least $0",
                 stock = "Probably none",
                 photo = "Void"):
        self.id = next(self._ids)
        self.name = name
        self.description = description
        self.cost = cost
        self.stock = stock
        self.photo = photo
        
    
books = [
    Book(name= "Tintin in America", cost= 25, stock= 7, photo= "https://images-na.ssl-images-amazon.com/images/I/912vIXwG23L.jpg"),
    Book(name= "Tintin and the Picaros", cost= 25, stock= 5, photo= "https://images-na.ssl-images-amazon.com/images/I/61%2Bp-97QRIL.jpg"),
    Book(name= "Tintin in America", cost= 25, stock= 7, photo= "https://images-na.ssl-images-amazon.com/images/I/912vIXwG23L.jpg"),
    Book(name= "Tintin in America", cost= 25, stock= 7, photo= "https://images-na.ssl-images-amazon.com/images/I/912vIXwG23L.jpg"),
    Book(name= "Tintin in America", cost= 25, stock= 7, photo= "https://images-na.ssl-images-amazon.com/images/I/912vIXwG23L.jpg"),
    Book(name= "Tintin in America", cost= 25, stock= 7, photo= "https://images-na.ssl-images-amazon.com/images/I/912vIXwG23L.jpg")
]

users = [
    User("Moses")
]

loged_user = users[0]

#Index page
@route('/')
@view('index')
def index():
    pass

#Store page
@route('/store')
@view('store')
def store():
    data = dict(books_list = books)
    return data

#Cart updated page
@route('/cart_updated/<book_id>')
@view('cart_updated')
def cart_updated(book_id):
    book_id = int(book_id)
    found_book = None
    for book in books:
        if book.id == book_id:
            found_book = book
            break
    found_book.stock -= 1
    data = dict(book = found_book)
    loged_user.books_in_cart.append(found_book)
    return data



run(host='0.0.0.0', port = 6969, reloader = True, debug = True)