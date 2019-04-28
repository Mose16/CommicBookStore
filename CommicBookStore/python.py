from bottle import run, route, view, get, post, request, static_file
from itertools import count


class User:
    _ids = count (0)
    books_in_cart = []
    name = None
    password = None
    admin = None
    
    def __init__(self, name, password, admin = False):
        self.id = next(self._ids)
        self.name = name
        self.password = password
        self.admin = admin
    
    
class Book:
    _ids = count (0)
    name = "How the heck would I know"
    description = "It seems no one cared enough to write a description."
    cost = "At least $0"
    stock = "Probably none"
    photo = "nopicture.jpg"
    
    def __init__(self, 
                 name = "How the heck would I know",
                 description = "It seems no one cared enough to write a description.",
                 cost = "At least $0",
                 stock = "Probably none",
                 photo = "nopicture.jpg"):
        self.id = next(self._ids)
        self.name = name
        self.description = description
        self.cost = cost
        self.stock = stock
        self.photo = photo
        
    
books = [
    Book(name= "Tintin In America", cost= 25, stock= 7, photo= "TintinInAmerica.jpg"),
    Book(name= "Tintin And The Picaros", cost= 25, stock= 5, photo= "TintinAndThePicaros.jpg"),
    Book(name= "Prisoners Of The Sun", cost= 23, stock= 11983, photo= "PrisonersOfTheSun.jpg"),
    Book(name= "The Seven Crystal Balls", cost= 50, stock= 2, photo= "TheSevenCrystalBalls.jpg"),
    Book(name= "The Shooting Star", cost= 20, stock= 8),
    Book(name= "Tintin In The Congo", cost= 30, stock= 10, photo= "TintinInTheCongo.jpg")
]

users = [
    User("Void", "Void", admin = False),
    User("Moses", "Lel", admin = True),
    User("Jeremey", "PooBumy69"),
    User("Tom", "PooBumy69+2")
]

logged_user = users[0]
def set_user(user):
    global logged_user
    logged_user = user #users[users.index(user)]




#Images
@route('/pictures/<filename>')
def upload_image(filename):
    return static_file(filename, root='./images')


###Pages

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

#Sing-up
@route('/sign_up')
@view('sign_up')
def sign_up():
    pass

#Sing-in
@route('/sign_in')
@view('sign_in')
def sign_in():
    pass

#Sign_in_success
@route('/sign_in_success', method = "POST")
@view('sign_in_success')
def sign_in_success():
    found_user = None
    print('hell')
    for u in users:
        if request.forms.get("name") == u.name:
            if request.forms.get("password") == u.password:
                found_user = u
                set_user(found_user)
                logged_user = found_user
                return dict(user = logged_user)
    return
        
#Sign_up_success
@route('/sign_up_success', method = "POST")
@view('sign_up_success')
def sign_up_success():
    name = request.forms.get("name")
    password = request.forms.get("password")
    
    users.append(User(name, password))
    set_user(users[-1])
    return dict(user = logged_user)

#Cart page
@route('/cart')
@view('cart')
def cart():
    return dict(cart = logged_user.books_in_cart)

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
    logged_user.books_in_cart.append(found_book)
    return dict(book = found_book)


#Admin page
@route('/admin')
@view('admin')
def admin():
    return dict(user = logged_user), dict(books_list = books)



run(host='0.0.0.0', port = 6969, reloader = True, debug = True)

