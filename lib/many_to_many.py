class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def __repr__(self):
        return f"<Author {self.name}>"

    # return all contracts for this author
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    # return all books for this author through contracts
    def books(self):
        return [contract.book for contract in self.contracts()]

    # sign a new contract with a book
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        return Contract(self, book, date, royalties)

    # total royalties earned
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def __repr__(self):
        return f"<Book {self.title}>"

    # NEW: return all contracts for this book
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    # (optional, but useful) return all authors for this book
    def authors(self):
        return [contract.author for contract in self.contracts()]



class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    def __repr__(self):
        return f"<Contract {self.author.name} ↔ {self.book.title} ({self.date}, {self.royalties}%)>"

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]