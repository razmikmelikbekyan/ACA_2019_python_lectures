import json
from pathlib import Path
from typing import Dict, List

USERS = "database/users.json"


def create_users_data():
    """
    Creates an empty json file for storing users data. If the file already exists, it should
    not do anything.
    """
    p = Path(USERS)
    if not p.exists():
        with open(USERS, 'w') as infile:
            pass


def get_all_users() -> Dict[str, List[str]]:
    """Returns all users data in a dict: {user: [user_books]}."""
    with open(USERS, 'r') as infile:
        try:
            return json.load(infile)
        except ValueError:
            return {}


def get_user_books(code: str) -> List[str] or str:
    """
    Finds user by its code in users database and returns it's books data: the list of books, which
    user have been taken from library. If user does not exist in user database, returns string:
    "user not in database".
    """
    all_users = get_all_users()
    return all_users.get(code, 'user not in database')


def add_user(code: str):
    """Adds given user to the database."""

    if not code or not isinstance(code, str) or len(code) != 6:
        raise ValueError('User code must be a string with length 6.')

    if not code.isalnum():
        raise ValueError('User code must be alphanumeric.')

    all_users = get_all_users()
    if code in all_users:
        raise ValueError('User already is in database.')

    all_users[code] = []

    with open(USERS, mode='w') as in_file:
        json.dump(all_users, in_file, indent=2)
    print('User is added.')


def delete_user(code: str):
    """Deletes user from database."""
    all_users = get_all_users()

    if code not in all_users:
        raise ValueError(f'The user with code="{code}" is not in database.')

    if all_users[code]:
        raise ValueError('User has not returned books.')

    all_users.pop(code)

    with open(USERS, 'w') as in_file:
        json.dump(all_users, in_file, indent=2)
    print('User is deleted.')


def get_book_from_library(user_code: str, book_code: str):
    """Gets book from library: adds book code to user books data."""

    all_users = get_all_users()

    if user_code not in all_users:
        raise ValueError(f'The user with code="{user_code}" is not in database.')

    all_users[user_code].append(book_code)

    with open(USERS, 'w') as in_file:
        json.dump(all_users, in_file, indent=2)
    print('User have been gotten book.')


def return_book_to_library(user_code: str, book_code: str):
    """Return book to library: deletes book code from user books data."""

    all_users = get_all_users()

    if user_code not in all_users:
        raise ValueError(f'The user with code="{user_code}" is not in database.')

    if book_code not in all_users[user_code]:
        raise ValueError(
            f'The user with code="{user_code}" does not have the book with code="{book_code}".')

    all_users[user_code].remove(book_code)

    with open(USERS, 'w') as in_file:
        json.dump(all_users, in_file, indent=2)
    print('User have been returned book.')
