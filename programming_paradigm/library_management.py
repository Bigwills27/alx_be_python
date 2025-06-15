class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self.__is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    return f'You have checked out "{title}".'
        return f'"{title}" is not available.'

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    return f'You have returned "{title}".'
        return f'"{title}" was not checked out.'


    def list_available_books(self):
        available_books = [book.title for book in self._books if book.is_available()]
        return available_books