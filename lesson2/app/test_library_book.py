import pytest
from book import Book
from library import Library
def test_add_book():
    lib = Library()
    book = Book("aaa", "hadasa")
    lib.add_book(book)
    assert book in lib.books

def test_add_user():
    lib = Library()
    lib.add_user("hadasa")
    assert  "hadasa" in lib.users


def test_check_out_book_success():
    library = Library()
    user = "hadasa"
    book = Book("Python", "aaa")
    library.add_user(user)
    library.add_book(book)
    prev_checked_out = len(library.checked_out_books)
    library.check_out_book(user, book)
    new_checked_out = len(library.checked_out_books)
    assert new_checked_out == prev_checked_out + 1
    assert user in library.checked_out_books
    assert library.checked_out_books[user] == book



def test_search_books_exact_match():
    library = Library()
    book = Book(title="blabla", author="hadasa")
    library.add_book(book)
    result = library.search_books("blabla")
    assert len(result) == 1
    assert result[0].title == "blabla"


def test_check_out_nonexistent_book():
    library = Library()
    library.add_user("hadasa")

    with pytest.raises(ValueError):
        library.check_out_book("book", "hadasa")


def test_add_user_empty_name():
    library = Library()

    with pytest.raises(ValueError):
        library.add_user("")


