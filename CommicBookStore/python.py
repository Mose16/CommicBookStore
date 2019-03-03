from bottle import run, route, view, get, post, request, static_file
from itertools import count


class Books:
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
        self.name = name
        self.description = description
        self.cost = cost
        self.stock = stock
        self.photo = photo
        
    
books = [
    Book(name= "Tintin in America", cost= 25, stock= 7, photo= "images/TintinInAmerica"),
    Book(name= "Tintin in America", cost= 25, stock= 7, photo= "images/TintinInAmerica"),
    Book(name= "Tintin in America", cost= 25, stock= 7, photo= "images/TintinInAmerica"),
    Book(name= "Tintin in America", cost= 25, stock= 7, photo= "images/TintinInAmerica"),
    Book(name= "Tintin in America", cost= 25, stock= 7, photo= "images/TintinInAmerica"),
    Book(name= "Tintin in America", cost= 25, stock= 7, photo= "images/TintinInAmerica")
]