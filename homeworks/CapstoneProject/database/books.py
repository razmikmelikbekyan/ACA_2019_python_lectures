from typing import Dict, List

BOOKS = "database/books.txt"


def create_books_data():
    """
    Creates an empty txt file for storing books data. If the file already exists, it should
    not do anything.
    """
    pass


def get_all_books() -> List[Dict]:
    """Returns all books data in a list, where each item in a list is one book."""
    pass


def find_book(code: str) -> Dict:
    """
    Finds book by its code in library and returns it's data in the form of dict. If the book is not
    in the library, return an empty dict.

    For example:
    {
        'code': 'a1254',
        'name': 'The Idiot',
        'author': 'Fyodor Dostoyevsky',
        'quantity': 4,
        'available_quantity': 2
    }
    """
    pass


def add_book(code: str, name: str, author: str, quantity: int):
    """Adds given book to the database, which is a txt file, where each row is book."""
    pass


def delete_book(code: str):
    """Deletes book from database."""
    pass


def _interact_with_user(code: str, increase: bool):
    """
    Helper function for interacting with user. It increases or decreases available_quantity by 1.
    """
    pass


def give_book_to_user(code: str):
    """
    Gives book to user from library: decreases book available_quantity by 1.
    """
    pass


def get_book_from_user(code: str):
    """
    Gets book from user back to library: increases book available_quantity by 1.
    """
    pass
