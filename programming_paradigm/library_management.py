class Book:
    def __init__(self, title, author):
        self.title =  title
        self.author = author
        self.__is_checked_out = False
    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False
    def check_out_book(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False
    
    

class Library:
    def __init__(self):
        self.__books = []
    def add_book(self, book):
        self.__books.append(book)
    
    def list_available_books(self):
        for book in self.__books:
            return (book)
    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title and not book.__is_checked_out:
                book.__is_checked_out = True
                return
    def return_book(self, title):
        for book in self.__books:
            if book.title == title and book.__is_checked_out:
                book.__is_checked_out = False
                return