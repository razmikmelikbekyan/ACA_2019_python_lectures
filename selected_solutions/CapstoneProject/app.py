import argparse
from pprint import pprint

from database.books import (create_books_data, get_all_books, add_book, find_book, delete_book,
                            give_book_to_user, get_book_from_user)
from database.users import (create_users_data, add_user, get_user_books, delete_user,
                            get_all_users, get_book_from_library, return_book_to_library)

possible_operations = [
    'get_all_books', 'add_book', 'find_book', 'delete_book',
    'get_all_users', 'add_user', 'get_user_books', 'delete_user',
    'get_book_from_library', 'return_book_to_library'
]

parser = argparse.ArgumentParser()

parser.add_argument('--o', type=str, required=True,
                    help='The operation which you want to perform.',
                    choices=possible_operations, metavar=' | '.join(possible_operations))
parser.add_argument('--book', type=str, help='Book code')
parser.add_argument('--name', type=str, help='Book name')
parser.add_argument('--author', type=str, help='Book author')
parser.add_argument('--quantity', type=int, help='Book quantity')
parser.add_argument('--user', type=str, help='User code')

if __name__ == '__main__':
    args = parser.parse_args()
    create_books_data()
    create_users_data()

    operation = args.o
    if operation == 'get_all_books':
        pprint(get_all_books())
    elif operation == 'add_book':
        add_book(args.book, args.name, args.author, args.quantity)
    elif operation == 'find_book':
        pprint(find_book(args.book))
    elif operation == 'delete_book':
        delete_book(args.book)
    elif operation == 'get_all_users':
        pprint(get_all_users())
    elif operation == 'add_user':
        add_user(args.user)
    elif operation == 'get_user_books':
        pprint(get_user_books(args.user))
    elif operation == 'delete_user':
        delete_user(args.user)
    elif operation == 'get_book_from_library':
        if get_user_books(args.user) == 'user not in database':
            raise ValueError(f'The user with code="{args.user}" is not in database. Please first '
                             f'call "add_user" operation.')

        give_book_to_user(args.book)
        get_book_from_library(args.user, args.book)
    else:
        if get_user_books(args.user) == 'user not in database':
            raise ValueError(f'The user with code="{args.user}" is not in database')

        return_book_to_library(args.user, args.book)
        get_book_from_user(args.book)
