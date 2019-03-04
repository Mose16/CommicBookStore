from bottle import run, route, view, get, post, request, static_file
from itertools import count

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
@route('/cart_updated', METHOD="POST")
@view('cart_updated')
def cart_updated():
    pass



run(host='0.0.0.0', port = 6969, reloader = True, debug = True)