from typing import Dict, List

USERS = "database/users.json"


def create_users_data():
    """
    Creates an empty json file for storing users data. If the file already exists, it should
    not do anything.
    """
    pass


def get_all_users() -> Dict[str, List[str]]:
    """Returns all users data in a dict: {user: [user_books]}."""
    pass


def get_user_books(code: str) -> List[str] or str:
    """
    Finds user by its code in users database and returns it's books data: the list of books, which
    user have been taken from library. If user does not exist in user database, returns string:
    "user not in database".
    """
    pass


def add_user(code: str):
    """Adds given user to the database."""
    pass


def delete_user(code: str):
    """Deletes user from database."""
    pass


def get_book_from_library(user_code: str, book_code: str):
    """Gets book from library: adds book code to user books data."""
    pass


def return_book_to_library(user_code: str, book_code: str):
    """Return book to library: deletes book code from user books data."""
    pass
