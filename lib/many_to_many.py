class Author:

    all = []
    
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("Author needs to be a string.")

    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]
    
    def books(self):
        return [item.book for item in Contract.all if item.author is self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([item.royalties for item in Contract.all if item.author is self])

    
class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise Exception("Title needs to be a string.")
    
    def contracts(self):
        return [item for item in Contract.all if item.book is self]
    
    def authors(self):
        return [item.author for item in Contract.all if item.book is self]


class Contract:

    all = []
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Author is not an Author object.")
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception("Book is a Book object.")
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception("Date needs to be a string.")
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception("Royalties needs to be an integer.")
    
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda c: c.date)