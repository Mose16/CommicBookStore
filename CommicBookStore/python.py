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
    Book(name= "Tintin In America", cost= 25, stock= 7, photo= "https://images-na.ssl-images-amazon.com/images/I/912vIXwG23L.jpg"),
    Book(name= "Tintin And The Picaros", cost= 25, stock= 5, photo= "https://images-na.ssl-images-amazon.com/images/I/61%2Bp-97QRIL.jpg"),
    Book(name= "Pristoners Of The Sun", cost= 23, stock= 11983, photo= "https://www.sbs.com.au/guide/sites/sbs.com.au.guide/files/styles/body_image/public/tt_14.jpg?itok=nocJ7UhB&mtime=1510616903"),
    Book(name= "The Seven Crystal Balls", cost= 50, stock= 2, photo= "https://www.dimanoinmano.it/img/166498/full/fumetti/fumetti-classici/tintin-the-seven-crystal-balls.jpg"),
    Book(name= "The Shooting Star", cost= 20, stock= 8, photo= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfDn2tOeZ0djqsMmrRolQWMnly6CtsElg3nxY3g-uT1eVlpJ8i4Q"),
    Book(name= "Tintin In The Congo", cost= 30, stock= 10, photo= "http://en.tintin.com/images/tintin/actus/actus/004442/tintin-Congo_coverEN.jpg")
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

#Sing-in
@route('/sign_in')
@view('sign_in')
def sign_in():
    data = dict(users_list = users)
    return data

#Sign_in_success
@route('/sign_in_success')
@view('sign_in_success')
def sign_in_success():
    pass


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