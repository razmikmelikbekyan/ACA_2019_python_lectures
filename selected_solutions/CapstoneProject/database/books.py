from pathlib import Path
from typing import Dict, List

BOOKS = "database/books.txt"


def create_books_data():
    """
    Creates an empty txt file for storing books data. If the file already exists, it should
    not do anything.
    """
    p = Path(BOOKS)
    if not p.exists():
        with open(BOOKS, 'w') as infile:
            pass


def _parse_from_line(line: str) -> Dict:
    """Helper function which parses one line of books.txt"""
    [code, name, author, quantity, available_quantity] = line.split(" $$ ")
    return {
        'code': code,
        'name': name,
        'author': author,
        'quantity': int(quantity),
        'available_quantity': int(available_quantity.replace('\n', ''))
    }


def _parse_to_line(code: str,
                   name: str,
                   author: str,
                   quantity: int,
                   available_quantity: int) -> str:
    """
    Helper function which parses given book data to the line, which can be added to the books.txt .
    """
    return " $$ ".join([code, name, author, str(quantity), str(available_quantity)]) + '\n'


def get_all_books() -> List[Dict]:
    """Returns all books data in a list, where each item in a list is one book."""
    with open(BOOKS, 'r') as in_file:
        return [_parse_from_line(line) for line in in_file]


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
    for book in get_all_books():
        if book['code'] == code:
            return book
    return {}


def add_book(code: str, name: str, author: str, quantity: int):
    """Adds given book to the database, which is a txt file, where each row is book."""

    if not code or not isinstance(code, str) or len(code) != 5:
        raise ValueError('Book code must be a string with length 5.')

    if not code.isalnum():
        raise ValueError('Book code must be alphanumeric.')

    if not name or not isinstance(name, str) or len(name) > 100:
        raise ValueError('Book name must be a string with maximum length 100.')

    if not name.isalnum():
        raise ValueError('Book name must be alphanumeric.')

    if not author or not isinstance(author, str) or len(author) > 45:
        raise ValueError('Book author must be a string with maximum length 45.')

    if not author.isalnum():
        raise ValueError('Book author must be alphanumeric.')

    if not quantity or not isinstance(quantity, int) or quantity <= 0:
        raise ValueError('Book quantity must be positive integer.')

    if find_book(code):
        raise ValueError('Book already in library.')

    with open(BOOKS, mode='a') as in_file:
        in_file.write(_parse_to_line(code, name, author, quantity, quantity))
    print('Book is added.')


def delete_book(code: str):
    """Deletes book from database."""
    book_data = find_book(code)

    if not book_data:
        raise ValueError(f'The book with code="{code}" is not in library.')

    if book_data['quantity'] != book_data['available_quantity']:
        raise ValueError('There are users, who have not returned books.')

    with open(BOOKS, 'r') as in_file:
        books = [line for line in in_file if line[:5] != code]

    with open(BOOKS, 'w') as in_file:
        in_file.writelines(books)
    print('Book is deleted.')


def _interact_with_user(code: str, increase: bool):
    """
    Helper function for interacting with user. It increases or decreases available_quantity by 1.
    """
    change = +1 if increase else -1

    books = []
    with open(BOOKS, 'r') as in_file:
        for line in in_file:
            if line[:5] == code:
                line_data = _parse_from_line(line)
                line_data['available_quantity'] += change
                line = _parse_to_line(*list(line_data.values()))
            books.append(line)

    with open(BOOKS, 'w') as in_file:
        in_file.writelines(books)


def give_book_to_user(code: str):
    """
    Gives book to user from library: decreases book available_quantity by 1.
    """

    book_data = find_book(code)

    if not book_data:
        raise ValueError(f'The book with code="{code}" is not in library.')
    elif book_data['available_quantity'] == 0:
        raise ValueError('Sorry there is no available book at this moment.')
    else:
        _interact_with_user(code, False)
        print('Book have been given to user.')


def get_book_from_user(code: str):
    """
    Gets book from user back to library: increases book available_quantity by 1.
    """

    book_data = find_book(code)

    if not book_data:
        raise ValueError(f'The book with code="{code}" is not in library.')
    else:
        _interact_with_user(code, True)
        print('Book have been gotten from user.')
